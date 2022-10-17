from app import views
from django.urls import path

urlpatterns = [
    path('create/', views.create_recipe, name='create-recipe'),
    path('list/', views.RecipeListView.as_view(), name='view-recipes'),
]
