from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()

router.register(r'category', views.CategoryViewSet, basename='categorys')
router.register(r'product', views.ProductViewSet, basename='products')

urlpatterns = router.urls