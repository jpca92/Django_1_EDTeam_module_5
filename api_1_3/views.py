from django.shortcuts import render
from rest_framework import generics

from .models import Category, Product, Client, Order, OrderProduct
from .serializers import (
    CategorySerializer, 
    ProductSerializer,
    ClientSerializer,
    CategoryProdctSerializer,
    OrderSerializer, 


    )

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ListCreateAPIView is used to handle both GET and POST requests
# for the same endpoint. It allows you to list all objects and create a new one
class ClientView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# RetriveUpdateDestoyAPIView is used to handle GET, PUT, PATCH and DELETE requests
class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    lookup_field = 'id'
    serializer_class = ClientSerializer

# CategoryProductsView is used to retrieve a single category and its related products
class CategoryProductsView(generics.ListAPIView):
    queryset = Category.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = CategoryProdctSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
