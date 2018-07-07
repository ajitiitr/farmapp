from django.db import models
from products.models import Product
from useraccount.models import User,UserAddress
# Create your models here.

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    imgurl = models.CharField(max_length=128)
    shipping_price = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    state = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'cart_items'

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    user_shipping_addr = models.ForeignKey(UserAddress,on_delete=models.SET_NULL,blank=True,null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    order_item_total = models.FloatField()
    order_shipping_charges = models.FloatField()
    order_tax = models.FloatField()

    class Meta:
        db_table = 'order'

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    imgurl = models.CharField(max_length=128)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    #date = orderdate

    class Meta:
        db_table = 'order_items'
