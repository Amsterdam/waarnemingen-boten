import logging

from django.core.management.base import BaseCommand

from ais.scraper import BoatTrackingScraper

log = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        log.info("Starting Scraper")
        BoatTrackingScraper().start()
        log.info("Scraping Done")
