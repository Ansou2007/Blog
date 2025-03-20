from django.urls import path
from .views import connexion,deconnexion

urlpatterns = [
       path('login/',connexion,name='login'),
       path('logout/', deconnexion, name='logout'),
]