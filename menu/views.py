from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.


@api_view(['GET'])
def getMenu(request):
    menuObjs = Menu.objects.all()
    category = request.GET.get('category')
    
    if category is not None:
        category = category.capitalize()
        menuObjs = menuObjs.filter(category=category)

    serializers = MenuSerializer(menuObjs, many=True)
    return Response({"status":"200","payload": serializers.data})
