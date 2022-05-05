from django.urls import include, re_path, path 

# local 
from . import views

app_name="producto_app" 

urlpatterns = [
    path('api/product/por-usuario/', 
         views.ListProductUser.as_view(), 
         name='product-producto_by_user'
         ), 
    # 
    # Crear
    path('api/product/create/',
         views.VehicleCreateView.as_view(), 
         name='vehicle-create'
    ), 
    # Actualizar
    path('api/product/update/<pk>/',
         views.VehicleRetriveUpdateView.as_view(), 
         name='vehicle-delete'
    ), 
    # Eliminar
    path('api/product/delete/<pk>/',
         views.VehicleDeleteView.as_view(), 
         name='vehicle-delete'
    ),
    # Detail
    path('api/product/detail/<pk>/',
         views.VehicleDetailView.as_view(), 
         name='vehicle-detail'
    )  
]
