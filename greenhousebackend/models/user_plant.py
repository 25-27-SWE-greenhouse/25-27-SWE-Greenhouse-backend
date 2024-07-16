from django.db import models
from .user import User
from .plant import Plant

class UserPlant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)