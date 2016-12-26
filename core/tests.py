from django.test import TestCase

# Create your tests here.
from core.models import VehiclesBrands


class VehiclesTestCase(TestCase):

    def setUp(self):
        VehiclesBrands.objects.create(name="BMW")

    def the_name_of_the_brand(self):
        BMW = VehiclesBrands.objects.get(name="BMW")
        self.assertEqual(BMW.name, "BMW")
