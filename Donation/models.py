from django.db import models

# Create your models here.
class Donation(models.Model):
    name    =   models.CharField(max_length=50,default="Anoyumus")
    phone   =   models.IntegerField(max_length=12,default="0")
    purpose =   models.CharField(max_length=300)
    amount  =   models.IntegerField(max_length=10,default="0")

    def __str__(self):
        return self.name