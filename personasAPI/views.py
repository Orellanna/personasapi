from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.response import Response

from personasAPI.models import Persona
from personasAPI.serializers import PersonaSerializer

# Create your views here.
class PersonaView(APIView):
    
    def post(self,request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje":"persona se guardo"},status=status.HTTP_201_CREATED)
        else:
            return Response({"mensaje":"se genero un error al leer la data"},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,id=None):
        if id: 
            persona = Persona.objects.get(id=id)
            serializer = PersonaSerializer(persona)
            return Response({"mensaje":"personas encontradas","personas":serializer.data},status=status.HTTP_200_OK)
        else:
            persona = Persona.objects.all()
            serializer = PersonaSerializer(persona, many=True)
            return Response({"mensaje":"personas encontradas","personas":serializer.data},status=status.HTTP_200_OK)
    
    def put(self,request, id):
        persona = Persona.objects.get(id=id)
        serializer = PersonaSerializer(persona, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje:":"persona se actualizo"},status=status.HTTP_200_OK)
        else:
            return Response({"mensaje:":"se genero un error al leer la data"},status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        persona = list(Persona.objects.filter(id=id).values())
        
        if len(persona) > 0:
            Persona.objects.filter(id=id).delete()
            return Response({"mensaje:":"persona se elimino"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"mensaje":"Persona no encontrada"},status=status.HTTP_200_OK)
        