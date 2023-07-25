from django.shortcuts import render
from rest_framework import generics
from .models import*
from .serializers import*
from rest_framework import renderers

# Create your views here.
# views for Cat
class CatList(generics.ListCreateAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatSerializer


class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatShop.objects.all()
    serializer_class = CatSerializer