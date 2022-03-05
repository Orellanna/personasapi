from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)
    dui = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    
    # def getNombre(self):
    #     return self.nombre
    
    # def getApellido(self):
    #     return self.apellido
    
    # def getFecha(self):
    #     return self.fecha
    
    # def getDui(self):
    #     return self.dui
    
    # def getTelefono(self):
    #     return self.telefono
    
    # def getDireccion(self):
    #     return self.direccion
        
    def __str__(self) -> str:
        return super().__str__() + self
    