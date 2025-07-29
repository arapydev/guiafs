from rest_framework import serializers
from .models import Category, Professional

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProfessionalSerializer(serializers.ModelSerializer):
    # Esto le dice al serializer que use el CategorySerializer 
    # para mostrar los datos de las categorías relacionadas.
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Professional
        fields = [
            'id', 
            'full_name', 
            'specialty', 
            'bio', 
            'phone_number', 
            'email', 
            'address', 
            'categories'
        ]