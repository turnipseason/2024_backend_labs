from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Scientist, Mineral, Book
from .serializers import ScientistSerializer, MineralSerializer, BookSerializer

class ScientistListCreateAPIView(generics.ListCreateAPIView):
    # so that we could store and send stuff.
    # ser. class is a required reserved name
    queryset = Scientist.objects.all()
    serializer_class = ScientistSerializer
    # pk by default; an attempt was made
    #lookup_field = Scientist.name

class ScientistRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scientist.objects.all()
    serializer_class = ScientistSerializer

class MineralListCreateAPIView(generics.ListCreateAPIView):
    queryset = Mineral.objects.all()
    serializer_class = MineralSerializer

class MineralRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mineral.objects.all()
    serializer_class = MineralSerializer

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
