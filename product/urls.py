from django.urls import path
from . import views
#define urls
urlpatterns = [
    path("", views.home, name='home'),#to run in / product
    path("productpage/", views.productpage, name ='productpage'),
    path("addproduct/", views.addproduct, name ='addproduct')
]