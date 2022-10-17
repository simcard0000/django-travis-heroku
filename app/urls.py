from app import views
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('create/', views.create_recipe, name='create-recipe'),
    path('list/', views.RecipeListView.as_view(), name='view-recipes'),
]
