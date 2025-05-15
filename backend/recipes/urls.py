from django.urls import path
from recipes.views import search_recipes

# URL configuration for the recipes app.
# The `urlpatterns` list routes URLs to views. For more information please see:
urlpatterns = [
    path('search/', search_recipes, name='search_recipes'),
]