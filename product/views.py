from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib import messages
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
            messages.add_message(request, messages.SUCCESS, "Category Added Successfully ! ")
            return redirect('/product/categorylist')
        else:
            messages.add_message(request, messages.ERROR, "Invalid form, fill out all the fields. ")
            return render(request, 'product/addcategory.html',{"form": form1})
    return render(request, "product/addcategory.html", {"form" : CategoryForm})
# we use one slash more in redirect than render!!!
def updatecategory(request, category_id):
    instance = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance = instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,"Updated Successfully")
            return redirect ('/product/categorylist')
        else:
            messages.add_message(request, messages.ERROR,"Verify all fields.")
            return render(request, '/product/updatecategory.html',{'form':form})
    context = {
            "form": CategoryForm(instance = instance)
        }
    return render(request, 'product/updatecategory.html', context)

def deletecategory(request, category_id):
    category = Category.objects.get(id = category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, "Deleted Successfully")
    return redirect('/product/categorylist')

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
            messages.add_message(request, messages.SUCCESS, "Product Added Successfully ! ")
            return redirect('/product/addproduct')
        else:
            messages.add_message(request, messages.ERROR, "Invalid form, fill out all the fields. ")
            return render(request, 'product/addproduct.html',{"form": form})
    return render(request, "product/addproduct.html", {"form" : ProductForm})

def updateproduct(request, product_id):
    instance = Product.objects.get(id=product_id)
    #context is used to show the form
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance = instance)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,"Updated Successfully")
            return redirect ('/product/productlist')
        else:
            messages.add_message(request, messages.ERROR,"Verify all fields.")
            return render(request, '/product/updateproduct.html',{'form':form})
    context = {
            "form": ProductForm(instance = instance)
        }
    return render(request, 'product/updateproduct.html', context)

def deleteproduct(request, product_id):
    product = Product.objects.get(id = product_id)
    product.delete()
    messages.add_message(request, messages.SUCCESS, "Deleted Successfully")
    return redirect('/product/productlist')