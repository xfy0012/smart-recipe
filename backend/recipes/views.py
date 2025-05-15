from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['POST'])
def search_recipes(request):
   
    user_igredients = request.data.get('user_ingredients', [])
   
    return Response({
        "message": "Search logic to be implemented", 
        "ingredients": user_igredients
        })