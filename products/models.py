from django.db import models

class Product(models.Model):
  title = models.CharField(max_length=120,null=True,blank=True)
  content = models.CharField(max_length=120,null=True,blank=True)
  price = models.DecimalField(max_digits=120,null=True,blank=True, decimal_places=2, default=0.00)
