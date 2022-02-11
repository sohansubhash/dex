from django.db import models

# Create your models here.
class Species(models.Model):
    dex_id = models.IntegerField()
    name = models.CharField(max_length=30)
    height = models.IntegerField()
    weight = models.IntegerField()
    color_id = models.IntegerField()


