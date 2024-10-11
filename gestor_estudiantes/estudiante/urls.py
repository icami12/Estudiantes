from django.urls import path
from gestor_estudiantes.estudiante import views

app_name= 'estudiante'

urlpatterns = [
    path('',views.lista_estudiantes, name='lista_estudiantes')
]
