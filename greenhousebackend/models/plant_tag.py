from django.db import models
from .plant import Plant
from .tag import Tag


class PlantTag(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)