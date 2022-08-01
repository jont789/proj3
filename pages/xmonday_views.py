from django.shortcuts import render
from django.http import HttpResponse
#import dictionary for choices
from listings.choices import price_choices, state_choices, bedroom_choices
#create a function for the index link to urls API route
from listings.models import Listing
#about page is mainly realtor=,so import rea;tor model
from realtors.models import Realtor


# create a function for the indes link to urls API route

##def index(request):
##   return HttpResponse("<h1>Hello</h1>")

# Create your views here.

def index(request):
    context={
        'listings':listings,
        'state_choices':state_choices,
        'price_choices':price_choices,
        "bedroom_choices":bedroom_choices
    }
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")
