from django.contrib import admin
from django.urls import path
from .views import guardar_capitulo, home, hollowknight, hollowplay, hollplay13, soulsborne, inicioses, listado, lista_dominio, guardar_capitulo, eliminar_video, modificar, modificar_capitulo, hollowlore, demons, form_login, login_view, logout_view
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', home, name="home"),
    path('hollowknight', hollowknight, name="hollowknight" ),
    path('hollowplay', hollowplay, name="hollowplay"),
    path('hollplay13/<str:id>', hollplay13, name= "hollplay13" ),
    path('soulsborne', soulsborne , name="soulsborne"),
    path('iniciosesion', inicioses, name="iniciosesion"),
    path('listado', listado, name="listado"),
    path('formregistro', lista_dominio, name="formregistro"),
    path('registro', guardar_capitulo, name="registro"),
    path('eliminar/<str:id>',eliminar_video,name="eliminar_video"),
    path('modificar_capitulo<str:id>', modificar, name="modificar_capitulo"),
    path('modificar',modificar_capitulo,name="modificar"),   
    path('hollowlore', hollowlore, name="hollowlore"),
    path('demons', demons, name="demons"),
    path('login/',form_login, name="login"),
    path('sesion/',login_view, name="sesion"),
    path('logout/',logout_view,name="logout"),
    
]