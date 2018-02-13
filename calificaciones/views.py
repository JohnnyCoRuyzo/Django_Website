from django.shortcuts import render
from django.views.generic import ListView, DetailView
from calificaciones.models import Semestres,Materias,Notas,SubNotas
from django.template import Context, RequestContext

# Create your views here.
def ListaSemestres(request): 
    return render(request, "calificaciones/historia.html", {'semestres': Semestres.objects.all(),
                                                            'papa': CalculoPAPA()})

def ListaMaterias(request,numero): 
    return render(request, "calificaciones/semestres.html", {'semestres': Semestres.objects.all().filter(Numero=int(numero)),
                                                             'materias': Materias.objects.all().filter(Semestre=Semestres.objects.all().filter(Numero=int(numero)).first()),
                                                             'papa': CalculoPAPA(),     
                                                             'pappi': CalculoPAPPI(numero)})

def ListaNotas(request,numero,codigo): 
    return render(request, "calificaciones/materias.html", {'semestres': Semestres.objects.all().filter(Numero=int(numero)),
                                                            'materias': Materias.objects.all().filter(Codigo=int(codigo)),
                                                            'notas': Notas.objects.all().filter(Materia=Materias.objects.all().filter(Codigo=int(codigo)).first()),
                                                            'papa': CalculoPAPA(),     
                                                            'pappi': CalculoPAPPI(numero),
                                                            'definitiva': CalculoDefinitiva(numero,codigo)} )
                         
def ListaSubNotas(request,numero,codigo,id): 
    return render(request, "calificaciones/notas.html", {'semestres': Semestres.objects.all().filter(Numero=int(numero)),
                                                         'materias': Materias.objects.all().filter(Codigo=int(codigo)),
                                                         'notas': Notas.objects.all().filter(Id=int(id)),
                                                         'subnotas': SubNotas.objects.all().filter(Notas=Notas.objects.all().filter(Id=int(id)).first()),
                                                         'papa': CalculoPAPA(),     
                                                         'pappi': CalculoPAPPI(numero),
                                                         'definitiva': CalculoDefinitiva(numero,codigo),
                                                         'notaParcial': CalculoNotaParcial(numero,codigo,id)} )

def CalculoPAPA():
    definitiva = 0
    creditos = 0
    suma = 0
    papa = 0
    for s in Semestres.objects.all():
        for m in Materias.objects.all().filter(Semestre=s):
            definitiva = 0
            for n in Notas.objects.all().filter(Materia=m):
                definitiva += float(n.Nota)*float(n.Porcentaje)/100
            creditos += int(m.Creditos)
            suma += definitiva*int(m.Creditos)
    papa = suma/creditos
    return round(papa,1)

def CalculoPAPPI(numero):
    definitiva = 0
    creditos = 0
    suma = 0
    pappi = 0
    for m in Materias.objects.all().filter(Semestre=Semestres.objects.all().filter(Numero=int(numero)).first()):
        definitiva = 0
        for n in Notas.objects.all().filter(Materia=m):
            definitiva += float(n.Nota)*float(n.Porcentaje)/100
        creditos += int(m.Creditos)
        suma += definitiva*int(m.Creditos)
    pappi = suma/creditos
    return round(pappi,1)

    
def CalculoDefinitiva(numero,codigo):
    definitiva = 0
    for n in Notas.objects.all().filter(Materia=Materias.objects.all().filter(Codigo=int(codigo)).first()):
        definitiva += float(n.Nota)*float(n.Porcentaje)/100
    return round(definitiva,1)
    
def CalculoNotaParcial(numero,codigo,id):
    notaP = 0
    for sn in SubNotas.objects.all().filter(Notas=Notas.objects.all().filter(Id=int(id).first())):
        notaP += float(sn.Nota)*float(sn.Porcentaje)/100
    return round(notaP,1)