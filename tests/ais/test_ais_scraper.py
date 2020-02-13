from unittest.mock import patch

from django.core.management import call_command
from django.test import TestCase, override_settings

from ais.models import WaternetSnapshot
from ais.scraper import EmptyResponse, InvalidCredentials, MissingEnvVariables


@override_settings(WATERNET_PASSWORD='test', WATERNET_USERNAME='test')
@patch('ais.scraper.WaternetScraper.requests', autospec=True)
class TestWaternetScraper(TestCase):

    @override_settings(WATERNET_PASSWORD=None, WATERNET_USERNAME=None)
    def test_missing_credentials(self, requests):
        with self.assertRaises(MissingEnvVariables):
            call_command('scrape_waternet')
        self.assertEqual(WaternetSnapshot.objects.count(), 0)

    def test_403_response(self, requests):
        requests.post().status_code = 403
        with self.assertRaises(InvalidCredentials):
            call_command('scrape_waternet')
        self.assertEqual(WaternetSnapshot.objects.count(), 0)

    def test_empty_response_fail(self, requests):
        requests.post().status_code = 200
        requests.get().json.side_effect = [[]]  # empty list response

        with self.assertRaises(EmptyResponse):
            call_command('scrape_waternet')
        self.assertEqual(WaternetSnapshot.objects.count(), 0)

    def test_ok(self, requests):
        requests.post().status_code = 200
        requests.get().json.side_effect = ['test']
        call_command('scrape_waternet')
        self.assertEqual(WaternetSnapshot.objects.count(), 1)
