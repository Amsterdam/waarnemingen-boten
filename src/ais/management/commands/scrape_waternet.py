import logging

from django.core.management.base import BaseCommand

from ais.scraper import WaternetScraper

log = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        log.info("Starting Scraper")
        WaternetScraper().start()
        log.info("Scraping Done")
