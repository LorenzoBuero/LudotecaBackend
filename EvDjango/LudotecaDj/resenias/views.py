from django.shortcuts import render
from .models import Project

# Create your views here.
def buscador_resenias(request):
    resenias = Project.objects.all()
    return render(request, "resenias/buscador-resenias.html", {'resenias': resenias})

def resenia (request, pk):
    resenia = Project.objects.get(id=pk)
    return render(request, "resenias/resenia.html", {'resenia': resenia})
