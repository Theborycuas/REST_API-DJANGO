from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serlizaliza un Campo para poder probar nuestro APIViews'''

    name = serializers.CharField(max_length=10)