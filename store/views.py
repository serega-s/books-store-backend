from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from store.models import Book
from store.permissions import IsOwnerOrStaffOrReadOnly
from store.serializers import BooksSerializer


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']

    def perform_create(self, serializer):
        # serializer.validated_data['owner'] = self.request.user
        serializer.save(owner=self.request.user)


class AuthView(TemplateView):
    template_name = 'oauth.html'
