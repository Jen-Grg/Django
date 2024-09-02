from django.urls import path
from . import views
#define urls
urlpatterns = [
    path("", views.home, name='home'),#to run in / product
    path("productpage/", views.productpage, name ='productpage'),
    path("addproduct/", views.addproduct, name ='addproduct'),
    path("productlist/", views.productlist, name ='productlist'),
    path("addcategory/", views.addcategory, name ='addcategory'),
    path("categorylist/", views.categorylist, name ='categorylist'),
]