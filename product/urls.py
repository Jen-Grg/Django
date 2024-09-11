from django.urls import path
from . import views
#define urls
urlpatterns = [
    path("",views.home, name = "home" ),
    path("productpage/", views.productpage, name ='productpage'),
    path("addproduct/", views.addproduct, name ='addproduct'),
    path("productlist/", views.productlist, name ='productlist'),
    path("addcategory/", views.addcategory, name ='addcategory'),
    path("categorylist/", views.categorylist, name ='categorylist'),
    path("updateproduct/<int:product_id>", views.updateproduct, name ='updateproduct'),
    path("deleteproduct/<int:product_id>", views.deleteproduct, name ='deleteproduct'),
    path("updatecategory/<int:category_id>", views.updatecategory, name ='updatecategory'),
    path("deletecategory/<int:category_id>", views.deletecategory, name ='deletecategory'),
]