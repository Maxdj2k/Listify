from rest_framework import serializers
from .models import Listify

class ListifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Listify 
        fields = ('id', 'title', 'description', 'completed')