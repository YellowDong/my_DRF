from django.shortcuts import render
from my_app.models import IpoInfo
from my_app.serializers import IpoInfoSerializer
from rest_framework import viewsets

# Create your views here.

class IpoInfoViewSet(viewsets.ModelViewSet):
    queryset = IpoInfo.objects.all()
    serializer_class = IpoInfoSerializer

