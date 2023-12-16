import base64

from app.models import User, Product, Comment, Follower, Favorite, Cart, CartItem
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    image_base64 = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'admin', 'image', 'description', 'sold', 'image_base64')

    def get_image_base64(self, obj):
        image = obj.image
        if image:
            with open(image.path, 'rb') as img_file:
                return base64.b64encode(img_file.read()).decode('utf-8')
        return None  # Modify this based on your handling of null/empty images

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'user_id', 'seen', 'brand', 'category', 'color')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'rating', 'user_id', 'seller_id')

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'follower', 'followed')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'user_id', 'product_id')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'items', 'price')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'user', 'product', 'price')