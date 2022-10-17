from django.db import models

# Create your models here.
class RecipeModel(models.Model):
    meal = models.CharField(max_length=200)
    recipe = models.CharField(max_length=1000)
    def __str__(self):
        return self.meal
