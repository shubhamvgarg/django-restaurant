from rest_framework import serializers
from .models import *

class MenuSerializer(serializers.ModelSerializer):

    class  Meta:
        model  = Menu
        fields = '__all__'
