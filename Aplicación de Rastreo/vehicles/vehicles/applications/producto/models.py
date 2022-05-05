from django.db import models
from django.conf import settings
# 
from .managers import ProductManager
#
from model_utils.models import TimeStampedModel


class Positions(models.Model):
    """ Representa las posiciones """
    # 
    position = models.CharField(
        'Tag', 
        max_length=120, 
        unique=True
    )

    class Meta:
        verbose_name = 'Posicion'
        verbose_name_plural = 'Posiciones'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.color)


class Vehicles(TimeStampedModel):
    """Modelo que representa a los vehiculos"""

    name = models.CharField(
        'Id de Vehículo', 
        max_length=100
    )
    description = models.TextField(
        'Placas',
        blank=True
    ) 
    
    position = models.CharField(
        'Tag', 
        max_length=120, 
        unique=True
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="usuario_vehiculo",
        #editable=False
    )
     
    objects = ProductManager()

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)