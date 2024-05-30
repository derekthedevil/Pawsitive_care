from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProductTable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    description=models.TextField(max_length=200)
    quantity = models.PositiveIntegerField(null=True)
    image=models.ImageField(upload_to="images")
    is_available =models.BooleanField(default=True)
    category = models.CharField(max_length=100)


class Payment_history(models.Model):
    id=models.CharField(primary_key=True,max_length=20)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")
    datetime = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField(null=True)

class Order_history(models.Model):
    payment_id = models.ForeignKey(Payment_history,on_delete=models.CASCADE,db_column="payment_id")
    uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column="user_id")
    product_id = models.ForeignKey(ProductTable,on_delete=models.CASCADE,db_column="product_id")
    price=models.PositiveIntegerField(null=True)
    quantity= models.PositiveIntegerField(null=True)
    date  = models.DateField(auto_now=True)
    address = models.TextField(max_length=100,null=True)