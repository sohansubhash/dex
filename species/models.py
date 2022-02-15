from django.db import models

# Create your models here.
class Species(models.Model):
    dex_id = models.IntegerField()
    name = models.CharField(max_length=30)
    genus = models.CharField(max_length=60)
    type_one = models.IntegerField()
    type_two = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    color_id = models.IntegerField()
    shape_id = models.IntegerField()
    evolves_from_dex_id = models.IntegerField()
    evolution_chain_id = models.IntegerField()
    capture_rate = models.IntegerField()
    habitat_id = models.IntegerField()
    base_experience = models.IntegerField()
    growth_rate_id = models.IntegerField()
    is_legendary = models.BooleanField(default=False)
    is_mythical = models.BooleanField(default=False)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special = models.IntegerField()
    speed = models.IntegerField()

    class Meta:
        ordering = ['dex_id']

    def __str__(self):
        return self.name + 'the ' + self.genus

class Types(models.Model):
    type_id = models.IntegerField()
    type_name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['type_id']

    def __str__(self):
        return self.type_name

class Colors(models.Model):
    color_id = models.IntegerField()
    color_name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['color_id']

    def __str__(self):
        return self.color_name

class Shapes(models.Model):
    shape_id = models.IntegerField()
    shape_name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['shape_id']

    def __str__(self):
        return self.shape_name

class Habitats(models.Model):
    habitat_id = models.IntegerField()
    habitat_name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['habitat_id']

    def __str__(self):
        return self.habitat_name
