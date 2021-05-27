from django.db import models

# Create your models here.

class My_User(models.Model):
    first_name=models.CharField(max_length=70,primary_key=True)
    last_name=models.CharField(max_length=70)
    mail=models.EmailField()
    password=models.CharField(max_length=60)
    user_name=models.CharField(max_length=70)

class My_post(models.Model):
    user=models.ForeignKey(My_User,on_delete=models.CASCADE,null=True)
    Text=models.CharField(max_length=500)
    created_date=models.DateField()
    updated_date=models.DateField()
