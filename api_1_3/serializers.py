from rest_framework import serializers
from .models import Category, Product, Client, Order, OrderProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.image.url
        return representation
    
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


"""serializers related tables and generic views"""
class CategoryProdctSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'products']

class OrderProductSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

# This serializer is used to create an order with its products
# It uses the OrderProductSerializer to handle the nested order_products
# It also calculates the subtotal for each product based on the quantity and price
class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['code', 'client', 'order_products']

    def create(self, validated_data):
        list_order_products = validated_data.pop('order_products')
        order = Order.objects.create(**validated_data)

        for obj in list_order_products:
            product = obj['product']
            quantity = obj['quantity']
            price = product.price
            subtotal = price * quantity

            OrderProduct.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=price,
                subtotal=subtotal
            )
        return order

"""
Views sets the serializer class to be used for the view
"""

