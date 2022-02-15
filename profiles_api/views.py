from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers
# Create your views here.


class HelloApiViews(APIView):
    '''API View de Prueba'''
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        '''Retorna la Lista de Caracteristicas del ApiView'''
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, put, delete)',
            'Es Similar a una vista tradicional de Django',
            'Nos da el Mayor control sobre la lógica de nuestra aplicación'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        '''CREA UN MENSAJE CON NUESTRO NOMBRE'''
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        '''MANEJA ACTUALIZACIÓN de UN OBJETO'''

        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''MANEJA ACTUALIZACIÓN PARCIAL de UN OBJETO'''

        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''Borrar UN OBJETO'''

        return Response({'method': 'DELETE'})