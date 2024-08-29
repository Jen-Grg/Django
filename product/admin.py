from django.contrib import admin
from . models import Product, Category
# Register your models(database) here.
admin.site.register(Product)
admin.site.register(Category)