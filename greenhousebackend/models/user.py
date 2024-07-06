from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=69)
    bio = models.CharField(max_length=69)
