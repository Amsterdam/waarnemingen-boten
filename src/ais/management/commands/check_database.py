import logging

from django.core.management.base import BaseCommand

from ais.models import WaternetSnapshot, Waternet

log = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        waternet_count = Waternet.objects.count()
        waternet_timestamp = Waternet.objects.order_by('-scraped_at').first().scraped_at

        snapshot_count = WaternetSnapshot.objects.count()
        snapshot_timestamp = WaternetSnapshot.objects.order_by('-scraped_at').first().scraped_at

        log.info(
            f"""
            Waternetsnapshot count: {snapshot_count}
            Latest Waternetsnapshot timestamp: {snapshot_timestamp}
            Waternet count: {waternet_count}
            Latest Waternet timestamp: {waternet_timestamp}
            """
        )
