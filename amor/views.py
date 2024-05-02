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
        

class PrtcliPostView(APIView):
    def post(self, request):
        # Récupérer les données du corps de la requête
        cliprt = request.data.get('cliprt')

        # Récupérer les données de la base de données en fonction des valeurs fournies
        pret = Prtcli.objects.filter(CLIPRT=cliprt)

        # Sérialiser les données récupérées
        serializer = PrtcliSerializer(pret, many=True)

        # Renvoyer les données sérialisées en réponse JSON
        return Response(serializer.data)

class PrtcliComptPostView(APIView):
    def post(self, request):
        # Récupérer les données du corps de la requête
        cliprt = request.data.get('cliprt')
        nooper = request.data.get('nooper')

        # Récupérer les données de la base de données en fonction des valeurs fournies
        pret = Prtcli.objects.filter(CLIPRT=cliprt, NOOPER=nooper)

        # Sérialiser les données récupérées
        serializer = PrtcliSerializer(pret, many=True)

        # Renvoyer les données sérialisées en réponse JSON
        return Response(serializer.data)        

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
                pr.cserv,
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
                'duree_mourabaha': p[7],
                'TOF': p[8]
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