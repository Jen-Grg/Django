#to create a form according to model
from django.forms import ModelForm
from . models import *
#to create form template use crispy forms
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #for certain fields only a limit can be set