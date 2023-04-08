from django.db import models
from uuid import uuid4
# Create your models here.

class Pizza(models.Model):
    id = models.IntegerField(primary_key=uuid4, editable=False)
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural="Pizza"
    

    def __str__(self):
        return self.name


class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='pizza')
    name = models.CharField(max_length=120)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural="Toppings"


    

