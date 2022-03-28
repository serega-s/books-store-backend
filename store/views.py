from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    