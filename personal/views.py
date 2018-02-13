from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'personal/index.html')

def contacto(request):
    return render(request,'personal/contacto.html')

def notas(request):
    return render(request,'personal/notas.html')