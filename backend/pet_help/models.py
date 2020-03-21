from django.db import models

class Pet(models.Model):
    id = models.CharField()
    name = models.CharField()
