from django.db import models

# Create your models here.
class CatShop(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
