from .models import *
from rest_framework import serializers 
from django.contrib.auth import authenticate
from rest_framework import generics

class SignUpSerializer(serializers.ModelSerializer):
     class Meta:
          model = NewUser
          fields = ('nom','prenom','phone','username','email','address','post')     

# ----------- login ---------- 
class MyTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active and not user.is_blocked:
            user.number_attempt=0
            user.save()
            return user
        
        elif user and user.is_active and user.is_blocked:
            # return Response('message')
            # return Response(serializers.errors)
            raise serializers.ValidationError({'message':'Compte blocké, veillez contacter l\'daministrateur'})
        
        try:
            obj= NewUser.objects.get(phone=data['username'])
            if obj.number_attempt<5:
                obj.number_attempt +=1
                print(obj.number_attempt)
                obj.save()
                raise serializers.ValidationError({'message':'Compte blocké, veillez contacter l\'daministrateur.'})
            else:
                obj.number_attempt +=1
                print(obj.number_attempt)
                obj.is_blocked=True
                obj.save()
                raise serializers.ValidationError({'message':'Compte blocké, veillez contacter l\'daministrateur.'})
        except:
            raise serializers.ValidationError({'message':'Informations invalides.'}) 

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('nom','prenom','phone','username','email','address','post','image','password')
        extra_kawargs = {
              'nom':{ 'required':True,"allow_blank":False},
              'prenom':{ 'required':True,"allow_blank":False},
              'phone':{ 'required':True,"allow_blank":False},
              'username':{ 'required':True,"allow_blank":False},
              'email':{ 'required':True,"allow_blank":False},
              'image':{ 'required':False,},
              'password':{ 'required':True,"allow_blank":False,'min_lenght':4}
         }    

class PrtcliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prtcli
        fields = '__all__'
        #('NOOPER', 'NUMSEQ','EXPL','VALIDE','DATJOUR','DATOPER','DATOPER', 'CLIPRT','CPTPRT')

class PrtcamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prtcamo
        fields = '__all__'




class MvtdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mvtd
        fields = ['compte', 'datoper', 'datval', 'mntdev', 'libelle', 'codopsc', 'expl', 'nooper']


