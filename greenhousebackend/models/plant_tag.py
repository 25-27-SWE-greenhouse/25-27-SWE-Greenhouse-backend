from django.db import models
from .plant import Plant
from .tag import Tag


class PlantTag(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)