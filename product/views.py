from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
# Create your views here.
#This is the main function to perform actions for database. We code in this file
#There is two types, function based views and class based views: class based views is easier ot use to create APIs but harder to debug than function based views
#Django performs in mvt pattern(model(database),views(function, class),template(frontend template is stored)) pattern unlike Java , PHP which uses nvc
#Django has a built in admin panel
def home(request):
    #.all() show everything in the database, to keep limit
    product = Product.objects.all().order_by('-id')[:4]
    context = {
        "product": product
    }
    return render(request, "product/index.html", context)

def productpage(request):
    product = Product.objects.all()
    context1 = {
        "products": product
    }
    return render(request,"product/products.html",context1)


def addproduct(request):
    return render(request, "product/addproduct.html", {"form" : ProductForm})

