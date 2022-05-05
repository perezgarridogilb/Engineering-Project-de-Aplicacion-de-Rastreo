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
    position = PositionsSerializer(many=True)
    
    # Meta para conectarse al modelo 
    class Meta: 
        model = Vehicles 
        fields = (
            '__all__'
        )
              
class ProcesoVehiculoSerializer(serializers.Serializer): 
    
    name = serializers.CharField() 
    description = serializers.CharField()   
    position = serializers.CharField()     
        
class VehicleSerializer(serializers.ModelSerializer): 
    
    # position = PositionsSerializer(many=True)
    
    class Meta: 
        model = Vehicles 
        fields = ( 
            '__all__'
        )            