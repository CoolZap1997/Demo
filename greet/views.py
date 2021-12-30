from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h3>A random index page</h3>")

def sayHello(request, name):
    return HttpResponse(f"<h3>Hello {name}</h3>")
