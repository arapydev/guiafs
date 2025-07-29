from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProfessionalViewSet

# Creamos un router y registramos nuestros viewsets con él.
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'professionals', ProfessionalViewSet)

# Las URLs de la API son determinadas automáticamente por el router.
urlpatterns = [
    path('', include(router.urls)),
]