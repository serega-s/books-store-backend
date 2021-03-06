from django.db.models import Count, Case, When, Avg, F
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet

from store.models import Book, UserBookRelation
from store.permissions import IsOwnerOrStaffOrReadOnly
from store.serializers import BooksSerializer, UserBookRelationSerializer


class BooksViewSet(ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Book.objects \
        .all() \
        .annotate(annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
                  # rating=Avg('userbookrelation__rate'),
                  owner_name=F('owner__username')) \
        .prefetch_related('readers') \
        .order_by('id')
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsOwnerOrStaffOrReadOnly]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_fields = ['price', 'author_name']

    def perform_create(self, serializer):
        # serializer.validated_data['owner'] = self.request.user
        serializer.save(owner=self.request.user)


class UserBookRelationView(UpdateModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = UserBookRelation.objects.all()
    serializer_class = UserBookRelationSerializer
    lookup_field = 'book'

    def get_object(self):
        obj, _ = UserBookRelation.objects.get_or_create(user=self.request.user, book_id=self.kwargs['book'])

        return obj


class AuthView(TemplateView):
    template_name = 'oauth.html'

# Annotate does an aggregation and returns a model with a additional given field
# Aggregate does an aggregation and returns a object only with a given field
