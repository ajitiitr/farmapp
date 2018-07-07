from django.db import models
from useraccount.models import User

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=256,blank=False)
    product_desc = models.CharField(max_length=256,)
    ratting_review = models.ManyToManyField(User,through='Review')
    image_url = models.CharField(max_length=512,blank=False)

    def __str__(self):
        return self.product_name
    class Meta:
        db_table = "product"

class ProductVariant(models.Model):
    product = models.ForeignKey(Product,on_delete = models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    name = models.CharField(max_length=32)
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'product_variant'


class Catagory(models.Model):
    name = models.CharField(max_length=32,blank=False)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'catagory'

class Review(models.Model):
    user = models.ForeignKey(User,on_delete = models.SET_NULL,blank=True, null=True)
    product = models.ForeignKey(Product,on_delete = models.SET_NULL,blank=True, null=True)
    comment = models.CharField(max_length=1024)
    ratting = models.IntegerField(1)

    class Meta:
        db_table = 'review'