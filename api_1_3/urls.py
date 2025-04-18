from django.urls import path 
from . import views

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('category/<int:id>/products/', views.CategoryProductsView.as_view()),
    path('products/', views.ProductListView.as_view()),
    path('clients/', views.ClientView.as_view()),
    path('clients/<int:id>/', views.ClientDetailView.as_view()),
    path('orders/', views.OrderCreateView.as_view()),
    

]