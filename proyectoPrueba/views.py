
from django.http import HttpResponse, request

def inicio(request):
    return HttpResponse("Hola que tal")