
from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone
# 
from .models import Vehicles

# Create your tests here.

class VehiclesModelTests(TestCase):
    
    def test_was_is_a(self):
        """
        was_published_last_time returns True for questions whose pub_date is in the past time
        """
        last_question = Vehicles(name="27775", description="JEEP-23456", position="(19.823558, -98.085938)")
        # Verificar que el resultado de aplicar el método was_published_last_time() sobre last_question es igual a verdad
        self.assertIs(last_question.check_num_placas_vehicle(), True)
        
    # def test_was_is_a1(self):
    #     """
    #     was_published_last_time returns True for questions whose pub_date is in the past time
    #     """
    #     last_question = Vehicles(name="27775", description="FORD-23456", position="(19.823558, -98.085938)", user=2)
    #     # Verificar que el resultado de aplicar el método was_published_last_time() sobre last_question es igual a verdad
    #     self.assertIs(last_question.was_published_last_time(), True)  
    #     
    # def test_was_is_a11(self):
    #     """
    #     was_published_last_time returns True for questions whose pub_date is in the past time
    #     """
    #         
    #     last_question = Vehicles(name="27775", description="HONDA-23456", position="(19.823558, -98.085938)", user=2)
    #     # Verificar que el resultado de aplicar el método was_published_last_time() sobre last_question es igual a verdad
    #     self.assertIs(last_question.was_published_last_time(), True)      

# def create_vehicle(name, description, position, user):
#     return Vehicles.objects.create(name=name, description=description, position=position, user=user)
