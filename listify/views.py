from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ListifySerializer
from .models import Listify

# Create your views here.

class listifyView(viewsets.ModelViewSet):
    serializer_class = ListifySerializer
    queryset = Listify.objects.all()