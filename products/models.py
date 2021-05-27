from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=70)
    weight_in_grams=models.IntegerField()
    price_in_rupees=models.IntegerField()
    created_at=models.DateField()
    updates_at=models.DateField()