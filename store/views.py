from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['price']