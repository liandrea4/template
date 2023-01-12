from rest_framework import serializers
from .models import TestModel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('id', 'title', 'description')