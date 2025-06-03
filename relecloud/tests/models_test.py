from django.test import TestCase
from relecloud.models import Destination, Cruise, InfoRequest, Review

class DestinationModelTest(TestCase):
    def test_create_destination(self):
        destination = Destination.objects.create(
            name="Bahamas",
            description="Beautiful tropical paradise",
            popularity=10
        )
        self.assertEqual(str(destination), "Bahamas")
        self.assertEqual(destination.popularity, 10)

class CruiseModelTest(TestCase):
    def test_create_cruise(self):
        cruise = Cruise.objects.create(
            name="Caribbean Cruise",
            description="Luxury cruise to the Caribbean"
        )
        self.assertEqual(str(cruise), "Caribbean Cruise")