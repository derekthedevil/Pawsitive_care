from django.db import models

# Create your models here.
class ProductTable(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    description=models.TextField(max_length=200)
    quantity = models.PositiveIntegerField()
    image=models.ImageField(upload_to="images")
    is_available =models.BooleanField(default=True)
    category = models.CharField(max_length=100,default="mobile")


