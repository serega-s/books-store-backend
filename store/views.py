from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']


def auth(request):
    return render(request, 'oauth.html')
