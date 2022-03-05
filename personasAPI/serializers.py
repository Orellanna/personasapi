from rest_framework import serializers
from personasAPI.models import Persona
from dataclasses import fields

class PersonaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Persona
        fields = ('id','nombre','apellido','fecha','dui','telefono','direccion')
    