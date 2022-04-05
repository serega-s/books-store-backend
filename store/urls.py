from django.urls import path
from rest_framework.routers import SimpleRouter

from store import views

router = SimpleRouter()
router.register(r'book', views.BooksViewSet)
router.register(r'book_relation', views.UserBookRelationView)

urlpatterns = [
    path('auth/', views.AuthView.as_view())
]

urlpatterns += router.urls
