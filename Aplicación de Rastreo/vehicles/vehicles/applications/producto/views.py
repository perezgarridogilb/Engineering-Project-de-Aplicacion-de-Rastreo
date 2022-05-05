
# apps de terceros
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    # Recupera y actualiza
    RetrieveUpdateAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#
from django.shortcuts import render

# local models
from .models import Vehicles
# local serialiozers
from .serializers import (
    ProductSerializer, 
    VehicleSerializer
)

class ListProductUser(ListAPIView):
    serializer_class = ProductSerializer 
    # Paquete drescifra token 
    authentication_classes = (TokenAuthentication,) 
    # Tipos de permisos en base a la autenticación 
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self): 
        # recuperando usuario
        print(5*"*")
        usuario = self.request.user
        print(usuario)
        return Vehicles.objects.productos_por_user(usuario)
    
class VehicleCreateView(CreateAPIView):
    
    # authentication_classes = (TokenAuthentication,)
    
    # permission_classes = [IsAuthenticated]
      
    serializer_class = VehicleSerializer
    
    # def create(self, request, *args, **kwargs):
    #     serializer = ProcesoVehiculoSerializer(data=request.data)  
    #     serializer.is_valid(raise_exception=True)
    #     
    #     # Registramos el vehiculo
    #     vehicle = Vehicles.objects.create(
    #         name=serializer.validated_data['name'],
    #         description=serializer.validated_data['description'],
    #         position=serializer.validated_data['position'],
    #         user=self.request.user,
    #     )
    #     
    #     vehicle.save()
    #     
    #     return Response({'res': 'exitosos'}) 

    

class VehicleDetailView(RetrieveAPIView):
     
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
     
    # Requiere saber de dónde lo va a recuperar 
    serializer_class = VehicleSerializer
    
    # queryset = Vehicle.objects.filter()
    queryset = Vehicles.objects.all() 
    
class VehicleDeleteView(DestroyAPIView): 
    
    authentication_classes = (TokenAuthentication,)
    
    permission_classes = [IsAuthenticated]
    
    serializer_class = VehicleSerializer
    queryset = Vehicles.objects.all()  
    
class VehicleUpdateView(UpdateAPIView):
    
    authentication_classes = (TokenAuthentication,)
    
    permission_classes = [IsAuthenticated]
    
    # El serializardor, con el cual va a recibir los datos
    serializer_class = VehicleSerializer
    
    # Deacuerdo al pk que queremos encontrar en el enlace
    queryset = Vehicles.objects.all()   
    
class VehicleRetriveUpdateView(RetrieveUpdateAPIView):
    
    authentication_classes = (TokenAuthentication,)
    
    permission_classes = [IsAuthenticated]
    
    # El serializardor, con el cual va a recibir los datos
    serializer_class = VehicleSerializer
    
    # Deacuerdo al pk que queremos encontrar en el enlace
    queryset = Vehicles.objects.all()
     
    