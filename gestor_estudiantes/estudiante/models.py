from django.db import models

class Curso(models.Model):
    nombre = models.CharField (max_length = 60)
    cantidad_horas = models.PositiveIntegerField ()
    
    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField (max_length = 40)
    apellido = models.CharField (max_length = 40)
    edad = models.PositiveIntegerField()
    nota_curso = models.DecimalField (max_digits=5, decimal_places = 2)
    curso_alumn = models.ForeignKey (Curso, on_delete = models.CASCADE)
        
    def obtenerNombreCompleto(self):
        if self.nombre and self.apellido:
            nombre_completo = f'{self.nombre}, {self.apellido}'
            return nombre_completo.strip()
        else:
            return 'Nombre completo no disponible'
