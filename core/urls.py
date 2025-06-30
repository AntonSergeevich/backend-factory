# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FactoryViewSet, UnitViewSet, EquipmentViewSet,
    index, hierarchy
)

# DRF-роутер для API
router = DefaultRouter()
router.register(r'factories', FactoryViewSet)
router.register(r'units',     UnitViewSet)
router.register(r'equipment', EquipmentViewSet)

urlpatterns = [
    # CRUD-API
    path('api/', include(router.urls)),

    # HTML-страницы
    path('', index, name='index'),
    path('hierarchy/<str:model>/<int:pk>/', hierarchy, name='hierarchy'),
]
