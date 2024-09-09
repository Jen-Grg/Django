from django.db import models
#to use foreign key to create a one to many relationship in this case for category of products
class Category(models.Model):
    category_name = models.CharField(max_length = 200, unique=True)
    def __str__(self):
        return self.category_name
#As soon as you make changes in the model file we must use the command makemigration and migrate
# Create your models here. We create database in this page using object
class Product(models.Model):
    product_name = models.CharField(max_length=100)#string
    product_price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()#textfield has no maximum length
    image = models.FileField(upload_to='static/uploads',null=True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, null=True)#to change field, we require null=True for migration

    def __str__(self):
        return self.product_name