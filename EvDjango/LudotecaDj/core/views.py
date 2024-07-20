from django.shortcuts import render

# def holis(request):
#    return render(request, "core/holiwis.html")

def index(request):
    return render(request, "core/Index.html")


def contacto(request):
    return render(request, "core/contacto.html")


def sobre_nosotros(request):
    return render(request, "core/sobre-nosotros.html")
# Create your views here.
