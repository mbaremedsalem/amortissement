from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError,APIException
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from utils.helpers import get_current_host
from django.core.mail import send_mail
from .models import *
from .serializer import *
from django.db import connection
from django.db.models import Max
from rest_framework import generics
from django.utils import timezone

# Create your views here.
class InvalidInformationException(APIException):
    status_code = 400
    default_detail = 'Informations invalides'

class MytokenManager(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response({
            'message': 'Information invalide',
            'status':status.HTTP_400_BAD_REQUEST, 
        })

        user = serializer.validated_data
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': 'login success',
            'status':status.HTTP_200_OK, 
            'access': str(refresh.access_token),
            'refresh_token': str(refresh),  
        })
        
@api_view(['POST'])
def register(request):
    data = request.data
    user = SignUpSerializer(data=data)

    if user.is_valid():
        if not NewUser.objects.filter(username=data['email']).exists():
            user = NewUser.objects.create(
                nom = data['nom'],
                prenom = data['prenom'],
                phone = data['phone'] ,
                email = data['email'] ,
                username = data['username'] ,
                password = make_password(data['password']),
                address = data['address'] ,
                post = data['post'] 
            )
            return Response({'message':'User Registered'},status=status.HTTP_201_CREATED)
        else:
            return Response({'message':'User already exists'},status=status.HTTP_400_BAD_REQUEST)    
    else:
        return Response({})

    
class PrtcliView(APIView):
    def get(self, request):
        # Récupérer tous les flux de la base de données
        pret = Prtcli.objects.all()

        # Sérialiser les flux récupérés
        serializer = PrtcliSerializer(pret, many=True)

        # Renvoyer les flux sérialisés en réponse JSON
        return Response(serializer.data)
        

#class PrtcliPostView(APIView):
    #def post(self, request):
        # Récupérer les données du corps de la requête
        #cliprt = request.data.get('cliprt')

        # Récupérer les données de la base de données en fonction des valeurs fournies
        #prtcli_data = Prtcli.objects.filter(CLIPRT=cliprt).values(

        #)
        # Calculer Nbr_Echeance
        #nbr_echeance = Prtcamo.objects.filter(TYPAMO='R').count()

        # Sérialiser les données récupérées
        #serializer = PrtcliSerializer(prtcli_data, many=True)

        #response_data = []
        #for data in prtcli_data:
            #response_data.append({
            #    'Numero_Dossier': data['NOOPER'],
            #    'Compte_client': data['CPTVUE'],
            #    'Date_Creation': data['DATOPER'],
            #    'Capital': data['MNTPRT'],
            #    'Marge': data['TOTINT'],
            #    'Type': 'type mourabaha',
           #     'Nbr_Echeance': data['CSERV'],
                #nbr_echeance
         #   })
        
        #return Response(response_data)

  ###
from django.db.models import Count

class PrtcliPostView(APIView):
    def post(self, request):
        # Récupérer les données du corps de la requête
        cliprt = request.data.get('cliprt')

        # Récupérer les données de la base de données en fonction des valeurs fournies
        prtcli_data = Prtcli.objects.filter(CLIPRT=cliprt).values('NOOPER', 'CPTVUE', 'DATOPER', 'MNTPRT', 'TOTINT', 'CSERV')

        # Calculer le nombre d'échéances (Nbr_Echeance) pour chaque NOOPER
        nbr_echeances = Prtcamo.objects.filter(TYPAMO='R', NOOPER__in=prtcli_data.values_list('NOOPER', flat=True)) \
                                        .values('NOOPER') \
                                        .annotate(counter=Count('NOOPER'))

        # Convertir en dictionnaire pour un accès plus facile
        nbr_echeances_dict = {item['NOOPER']: item['counter'] for item in nbr_echeances}

        response_data = []
        for data in prtcli_data:
            nooper = data['NOOPER']
            response_data.append({
                'Numero_Dossier': nooper,
                'Compte_client': data['CPTVUE'],
                'Date_Creation': data['DATOPER'],
                'Capital': data['MNTPRT'],
                'Marge': data['TOTINT'],
                'Type': 'type mourabaha',
                'Nbr_Echeance': nbr_echeances_dict.get(nooper, 0),  # Utiliser le compteur calculé
            })

        # Renvoyer les données en réponse JSON
        return Response(response_data)

  ###
class PrtcliComptPostView(APIView):
    def post(self, request):
        # Récupérer les données du corps de la requête
        cliprt = request.data.get('cliprt')
        nooper = request.data.get('nooper')

        # Récupérer les données de Prtcli
        prtcli_data = Prtcli.objects.filter(CLIPRT=cliprt, NOOPER=nooper).values(
 
        )

        # Calculer Nbr_Echeance
        nbr_echeance = Prtcamo.objects.filter(NOOPER=nooper, TYPAMO='R').count()

        serializer = PrtcliSerializer(prtcli_data, many=True)
        # Construire la réponse
 
        response_data = []
        for data in prtcli_data:
            response_data.append({
                'Numero_Dossier': data['NOOPER'],
                'Compte_client': data['CPTVUE'],
                'Date_Creation': data['DATOPER'],
                'Capital': data['MNTPRT'],
                'Marge': data['TOTINT'],
                'Type': 'type mourabaha',
                'Nbr_Echeance': nbr_echeance
                #data['CSERV'],
            })
        # Renvoyer les données en réponse JSON
        return Response(response_data)

class PrtcamoliView(APIView):
    def get(self, request):
        # Récupérer tous les flux de la base de données
        amortissement = Prtcamo.objects.filter(TYPAMO='R')

        # Sérialiser les flux récupérés
        serializer = PrtcamoSerializer(amortissement, many=True)

        # Renvoyer les flux sérialisés en réponse JSON
        return Response(serializer.data)        

class PrtcamoNOOPERliView(APIView):
    def post(self, request):
        # Récupérer les données du corps de la requête
        nooper = request.data.get('nooper')

        # Récupérer les données de la base de données en fonction des valeurs fournies
        amortissement = Prtcamo.objects.filter(NOOPER=nooper,TYPAMO='R')

        # Sérialiser les données récupérées
        serializer = PrtcamoSerializer(amortissement, many=True)

        # Renvoyer les données sérialisées en réponse JSON
        return Response(serializer.data)         



class entetPostView(APIView):
    def post(self, request):
        # Récupérer les données du corps de la requête
        cliprt = request.data.get('cliprt')
        nooper = request.data.get('nooper')

        # Exécuter la requête SQL personnalisée
        query = """
            SELECT 
                pr.nooper AS Numero_Dossier,
                'type mourabaha' AS type_mourabaha,
                pr.datdep AS date_mep,
                pr.datrmb AS date_1ech,
                MAX(ech.datrmb) AS date_dern_ech,
                MAX(pr.mntprt) AS prix_achat,
                MAX(pr.mntprt) + SUM(ech.mntint) AS prix_vente,
                MAX(pr.mntprt) + SUM(ech.mntint) + SUM(mnttaxe) AS prix_venteTTC,
                pr.mnttaxdos AS frais_dossier,
                pr.mntasf AS frais_detude,
                COUNT(*) AS duree_mourabaha,
                pr.txtaxe AS TOF
            FROM 
                prtcli pr
            JOIN
                prtcamo ech ON pr.nooper = ech.nooper AND ech.typamo = 'R'
            WHERE 
                pr.cliprt = %s AND pr.nooper = %s
            GROUP BY 
                pr.nooper,
                pr.datdep,
                pr.datrmb,
                pr.mnttaxdos,
                pr.mntasf,
                pr.txtaxe
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [cliprt, nooper])
            pret = cursor.fetchall()

        # Créer un dictionnaire de résultats
        results = []
        for p in pret:
            results.append({
                'Numero_Dossier': p[0],
                'Type_De_Pret': p[1],
                'date_mep': p[2],
                'date_1ech': p[3],
                'date_dern_ech': p[4],
                'prix_achat': p[5],
                'prix_vente': p[6],
                'prix_vente_TTC': p[7],
                'frais_dossier': p[8],
                'frais_detude': p[9],
                'duree_mourabaha': p[10],
                'TOF': p[11]
            })

        # Renvoyer les données sérialisées en réponse JSON
        return Response(results)


class entetPostView2(APIView):
    def post(self, request):
        # Récupérer les données du corps de la requête
        cliprt = request.data.get('cliprt')
        nooper = request.data.get('nooper')

        # Exécuter la nouvelle requête SQL personnalisée
        query = """
        SELECT 
            pr.nooper AS Numero_Dossier,
            'type mourabaha' AS type_mourabaha,
            pr.datdep AS date_mep,
            pr.datrmb AS date_1ech,
            MAX(ech.datrmb) AS date_dern_ech,
            MAX(pr.mntprt) AS prix_achat,
            SUM(pr.mntprt + ech.mntint) AS prix_vente,
            pr.cserv AS duree_mourabaha,
            pr.txtaxe AS TOF
        FROM 
            prtcli pr
        JOIN
            prtcamo ech ON pr.nooper = ech.nooper 
        WHERE 
            pr.cliprt = %s AND pr.nooper = %s
        GROUP BY 
            pr.nooper,
            pr.datdep,
            pr.datrmb,
            ech.datrmb,  -- Inclure ech.datrmb dans GROUP BY
            pr.mntprt,   -- Inclure pr.mntprt dans GROUP BY
            pr.cserv,
            pr.txtaxe;
        """

        # Exécuter la requête SQL
        with connection.cursor() as cursor:
            cursor.execute(query, [cliprt, nooper])
            results = cursor.fetchall()

        # Créer un dictionnaire de résultats
        data = []
        for row in results:
            data.append({
                'Numero_Dossier': row[0],
                'type_mourabaha': row[1],
                'date_mep': row[2],
                'date_1ech': row[3],
                'date_dern_ech': row[4],

                'duree_mourabaha': row[7],
                'TOF': row[8]
            })

        # Renvoyer les données sérialisées en réponse JSON
        return Response(data)        


class MvtdListView(generics.ListAPIView):
    queryset = Mvtd.objects.all()
    serializer_class = MvtdSerializer


class MvtdSpecificDateListView(APIView):
    def post(self, request):
        date = request.data.get('date', None)
        if date is None:
            return Response({"error": "Date is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        mvtd_queryset = Mvtd.objects.filter(datoper__lt=date)
        serializer = MvtdSerializer(mvtd_queryset, many=True)
        return Response(serializer.data)

class MvtdSpecificNooperListView(APIView):
    def post(self, request):
        nooper = request.data.get('nooper', None)
        if nooper is None:
            return Response({"error": "Nooper is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        mvtd_queryset = Mvtd.objects.filter(nooper=nooper)
        serializer = MvtdSerializer(mvtd_queryset, many=True)
        return Response(serializer.data)

class MvtdCurrentDateListView1(generics.ListAPIView):
    serializer_class = MvtdSerializer

    def get_queryset(self):
        current_date = timezone.now().date()
        return Mvtd.objects.filter(datoper__lt=current_date)        