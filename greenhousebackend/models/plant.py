from django.db import models
from .tag import Tag

class Plant(models.Model):
    name = models.CharField(max_length=55)
    species = models.CharField(max_length=55)
    image_URL = models.URLField(max_length=200, blank=True, null=True)
    tags =  models.ForeignKey(Tag, on_delete=models.CASCADE)