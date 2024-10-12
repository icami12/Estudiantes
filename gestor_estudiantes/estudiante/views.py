from django.shortcuts import get_object_or_404, render
from gestor_estudiantes.estudiante.models import Curso, Estudiante

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    
    lista_estud = []
    for estud in estudiantes:
        if estud.nombre and estud.apellido:
            nombre_completo = f'{estud.nombre}, {estud.apellido}'
            infoEstudiante = {
                'nombre': nombre_completo.strip(),
                'edad': estud.edad,
                'nota': estud.nota_curso,
                'nombCurso': estud.curso_alumn.nombre if estud.curso_alumn else 'Sin curso'
            }
            lista_estud.append(infoEstudiante)
        else:
            lista_estud.append({'error':'Registro alumno incompleto'})
    return render(request, 'estudiante/lista_estudiantes.html',{'estudiantes':lista_estud})

def lista_estudMayoresAEdad(request,pk):
    estudiantes = Estudiante.objects.filter(edad__gt=pk)
    
    return render(request, 'estudiante/estudiantesMayoresAUnaEdad.html',{'estudiantes':estudiantes})

def info_curso(request, pk):
    curso = get_object_or_404(Curso, id=pk)
    return render(request, 'estudiante/buscarCurso.html',{'curso':curso})
            
    
    
