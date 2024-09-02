from django.shortcuts import render, redirect
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

def categorylist(request):
    category = Category.objects.all()
    context = {
        "category": category
    }
    return render(request,"product/categorylist.html",context)

def addcategory(request):
    if request.method == "POST":
        form1 = CategoryForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/product/categorylist')
        else:
            return render(request, 'product/addcategory.html',{"form": form1})
    return render(request, "product/addcategory.html", {"form" : CategoryForm})

def productlist(request):
    product = Product.objects.all()
    context1 = {
        "product": product
    }
    return render(request,"product/productlist.html",context1)

def addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product/productlist')
        else:
            return render(request, 'product/addproduct.html',{"form": form})
    return render(request, "product/addproduct.html", {"form" : ProductForm})

