from django.shortcuts import render
from rest_framework import generics
from .serializers import TestSerializer
from .models import TestModel

# Create your views here.


class TestView(generics.ListAPIView):
    serializer_class = TestSerializer
    queryset = TestModel.objects.all()