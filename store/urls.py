from django.urls import path
from rest_framework.routers import SimpleRouter

from store import views

router = SimpleRouter()
router.register(r'book', views.BooksViewSet)

urlpatterns = [
    path('auth/', views.AuthView.as_view())
]

urlpatterns += router.urls
