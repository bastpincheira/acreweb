from django.db.models.base import Model

from rest_framework import serializers

from acre.models import Capitulo

class CapituloSerializador(serializers.ModelSerializer):

    class Meta:

        model = Capitulo

        fields = ['idcapitulo','nomcapitulo','numcapitulo','url','imgcap','dominio','seccion']