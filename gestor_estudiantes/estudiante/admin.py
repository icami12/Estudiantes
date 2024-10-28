from django.contrib import admin
from .models import Estudiante, Curso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_horas')  
    search_fields = ('nombre', 'cantidad_horas')

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'curso_alumn', 'nota_curso') 
    search_fields = ('nombre', 'apellido', 'curso_alumn')
    
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Curso, CursoAdmin)