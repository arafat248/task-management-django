from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(rwquest):
    return HttpResponse("Hello world")

def home (request):
    return render (request, "home.html")

def dynamic_urls(request, id):
    return HttpResponse (f"dynamic urls {id}")