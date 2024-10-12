from django.urls import path
from gestor_estudiantes.estudiante import views

app_name= 'estudiante'

urlpatterns = [
    path('estudiantes/',views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/mayores_de/<int:pk>/',views.lista_estudMayoresAEdad, name='lista_estudiantesMayoresAUnaEdad'),
    path('curso_detalle/<int:pk>/',views.info_curso, name='buscarCurso')
]
