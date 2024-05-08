from rest_framework import serializers
from .models import Scientist, Mineral, Book

class ScientistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientist
        fields = '__all__'
class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mineral
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    # no values err if no Meta
    class Meta:
        model = Book
        fields = '__all__'
