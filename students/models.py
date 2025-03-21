from django.db import models

# Create your models here.
class Student (models.Model) :
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)