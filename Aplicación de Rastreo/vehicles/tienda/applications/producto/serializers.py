from rest_framework import serializers 
# 
from .models import Vehicles, Positions 

class PositionsSerializer(serializers.ModelSerializer): 
    
    # Meta para conectarse al modelo 
    class Meta: 
        model = Positions 
        fields = (
            'color', 
        )

class ProductSerializer(serializers.ModelSerializer): 
    
    # many: Más de un objeto 
    colors = PositionsSerializer(many=True)
    
    # Meta para conectarse al modelo 
    class Meta: 
        model = Vehicles 
        fields = (
            'name', 
            'description',
            'man',
            'woman',
            'weight',
            'price_purchase',
            'price_sale',
            'main_image',
            'image1',
            'image2',
            'image3',
            'image4',
            'colors',
            'video',
            'stok',
            'num_sales',
        )