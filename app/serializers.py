from rest_framework import serializers
from .models import RecipeModel

class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = ('meal', 'recipe',"id") # fields in the models
