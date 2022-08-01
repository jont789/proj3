from django.shortcuts import render
from django.http import HttpResponse

##from listings.choices import price_choices, state_choices, bedroom_choices


# create a function for the indes link to urls API route

##def index(request):
##   return HttpResponse("<h1>Hello</h1>")

# Create your views here.

def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")
