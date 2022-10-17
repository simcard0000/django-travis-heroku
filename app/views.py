from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import RecipeListSerializer
from rest_framework.response import Response
from .models import RecipeModel

@api_view(['POST'])
def create_recipe(request):
        # create recipe
    recipe = RecipeListSerializer(data=request.data)
    if recipe.is_valid():
        recipe.save()
        return Response(recipe.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

class RecipeListView(generics.ListCreateAPIView):
    # list out recipes
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeListSerializer
