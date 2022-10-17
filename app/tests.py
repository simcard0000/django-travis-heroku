from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from app.models import RecipeModel
from django.urls import reverse
from app.serializers import RecipeListSerializer

RECIPES_URL = reverse('app:view-recipes')

def sample_recipe(**params):
    """Create and return a sample recipe"""
    defaults = {
        'meal': 'Sample recipe',
        'recipe': "Sample recipe detail",
    }
    defaults.update(params)

    return RecipeModel.objects.create(**defaults)

class RecipeApiTests(TestCase):
    """Test recipe retrieval API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_recipes(self):
        """Test retrieving a list of recipes"""
        sample_recipe()
        sample_recipe()
        res = self.client.get(RECIPES_URL)

        recipes = RecipeModel.objects.all()
        serializer = RecipeListSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
