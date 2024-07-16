from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=55)
    species = models.CharField(max_length=55)