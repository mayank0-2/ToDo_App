from django.db import models

# Create your models here.

class todo_model(models.Model):
    title = models.CharField(max_length=30, unique= True, blank=False)
    description = models.TextField()
    date = models.DateField(blank= False)