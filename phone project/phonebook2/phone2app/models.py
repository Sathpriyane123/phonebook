from django.db import models

# Create your models here.
class Phonebook(models.Model):
    name=models.CharField(max_length=60)
    phone=models.IntegerField(max_length=60)

def __str__(self):
    return self.name
    
