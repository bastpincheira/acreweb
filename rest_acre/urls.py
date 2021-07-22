from django.urls import path

from .views import lista_capitulo, manipular_capitulo
from .viewslogin import login


urlpatterns = [

    path('lista_capitulo',lista_capitulo,name="lista_capitulo"),
    path('manipular_capitulo/<id>',manipular_capitulo,name="manipular_capitulo"),
    path('loginRest',login,name="loginRest"),

]