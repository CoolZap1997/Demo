from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import PersonForm

# Create your views here.
def index(request):
    return HttpResponse("<h3>A random index page</h3>")

def sayHello(request, name):
    return HttpResponse(f"<h3>Hello {name}</h3>")

@csrf_protect
def addPerson(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if(form.is_valid()):
            form.save()
            return render(request, "greet/add_success.html")
        else:
            return render(request, "greet/add_failed.html")
    else:
        form = PersonForm()
        return render(request, "greet/add_person.html", {'form':form})

