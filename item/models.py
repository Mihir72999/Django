from django.db import models

# Create your models here.


class Item(models.Model):
     id = models.AutoField
     name = models.CharField(max_length=200)
     price = models.IntegerField(default=99)
     image = models.CharField(max_length=500)
     available_Qty = models.IntegerField(default=1)
     brand=models.CharField(max_length=60 , default="")
     brandmodel = models.CharField(max_length=100 ,default="apple")

     def __str__(self):
          return self.name