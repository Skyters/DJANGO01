from django.db import models

# Create your models here.

class Client(models.Model):
        name = models.TextField()
        telephone=models.TextField()
        Date_birth=models.DateField()
        Loyalty_status=models.TextField()                