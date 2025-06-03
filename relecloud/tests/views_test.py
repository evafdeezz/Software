from django.test import TestCase, Client
from django.urls import reverse
from relecloud.models import Destination

class DestinationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.destination = Destination.objects.create(
            name="Bahamas",
            description="Beautiful tropical paradise"
        )

    def test_destinations_view(self):
        response = self.client.get(reverse('destinations'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bahamas")