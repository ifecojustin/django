from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def lota(request):
    return HttpResponse("Hello, Lota!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name":name.capitalize()
    })
    # return HttpResponse(f"Hello, {name.capitalize()}!")