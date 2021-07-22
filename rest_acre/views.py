from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.utils import serializer_helpers
from acre.models import Capitulo
from .serializers import CapituloSerializador
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated
# Create your views here.
@csrf_exempt

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_capitulo(request):
    if request.method == 'GET':

        m = Capitulo.objects.all()

        serializer = CapituloSerializador(m, many = True)

        return Response(serializer.data)



    elif request.method == 'POST':

        data2 = JSONParser().parse(request)

        serializer = CapituloSerializador(data = data2)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status = status.HTTP_201_CREATED)

        else:

            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def manipular_capitulo(request,id):

    try:

        m = Capitulo.objects.get(idcapitulo = id)

    except Capitulo.DoesNotExist:

        return Response(status= status.HTTP_404_NOT_FOUND)

    

    if request.method == 'GET':

        serializer = CapituloSerializador(m)

        return Response(serializer.data)



    elif request.method == 'PUT':

        data2 = JSONParser().parse(request)

        serializer = CapituloSerializador(m, data = data2)



        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        else:

            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    elif request.method == 'DELETE':

        m.delete()

        return Response(status= status.HTTP_204_NO_CONTENT)            