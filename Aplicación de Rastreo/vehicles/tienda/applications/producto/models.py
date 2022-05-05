from django.db import models
from django.conf import settings
# 
from .managers import ProductManager
#
from model_utils.models import TimeStampedModel


class Positions(models.Model):
    """ Representa color de un producto """

    color = models.CharField(
        'Tag', 
        max_length=120, 
        unique=True
    )
    #

    class Meta:
        verbose_name = 'Posicion'
        verbose_name_plural = 'Posiciones'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.color)


class Vehicles(TimeStampedModel):
    """Modelo que representa a un producto de tienda"""

    name = models.CharField(
        'Nombre', 
        max_length=100
    )
    description = models.TextField(
        'Descripcion vehiculo',
        blank=True
    )
    man = models.BooleanField(
        'Para Hombre', 
        default=True
    ) # es solo para mujer 
    woman = models.BooleanField(
        'Para Mujer', 
        default=True
    ) # es para varon
    weight = models.DecimalField(
        'Peso', 
        max_digits=5, 
        decimal_places=2, 
        default=1
    )
    price_purchase = models.DecimalField(
        'Precio de Compra',
        max_digits=10,
        decimal_places=3
    )
    price_sale = models.DecimalField(
        'Precio de Venta',
        max_digits=10,
        decimal_places=2
    )
    main_image = models.ImageField(
        'imagen principal',
        upload_to='producto',
    ) # imagen principal del producto
    image1 = models.ImageField('Imagen 1', blank=True, null=True)
    image2 = models.ImageField('Imagen 2', blank=True, null=True)
    image3 = models.ImageField('Imagen 3', blank=True, null=True)
    image4 = models.ImageField('Imagen 4', blank=True, null=True)
    colors = models.ManyToManyField(Positions)
    video = models.URLField('unboxin', blank=True, null=True)
    stok = models.PositiveIntegerField('Stok', default=0)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="prod_created",
    )
    
    objects = ProductManager()

    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)