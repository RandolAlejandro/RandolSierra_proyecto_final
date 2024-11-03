from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=20)
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.anio}"
    
