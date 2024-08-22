from django.urls import path
from .views import *


urlpatterns = [
        path('login/', MytokenManager.as_view(), name='token_obtain_pair'),
        path('register/', register, name='register'),

        path('get-amotissement/', PrtcamoliView.as_view(), name='get-amortissement'),
        path('get-amotissement-by-nooper/', PrtcamoNOOPERliView.as_view(), name='get-amortissement-bynooper'),
        
        path('get-pret/', PrtcliView.as_view(), name='get-pret'),
        path('get-pret-cli/', PrtcliPostView.as_view(), name='get_pret_cli'),
        path('get-pret-cli-compte/', PrtcliComptPostView.as_view(), name='get_pret_cli_compte'),

        path('get-entet-cli/', entetPostView.as_view(), name='get_entet_cli'),

        
        path('mvtd/', MvtdListView.as_view(), name='mvtd-list'),
        path('mvtd/specific-date/', MvtdSpecificDateListView.as_view(), name='mvtd-date'),
        path('mvtd/specific-nooper/', MvtdSpecificNooperListView.as_view(), name='mvtd-nooper'),

        

        
]