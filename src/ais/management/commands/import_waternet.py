import logging

from django.core.management.base import BaseCommand

from ais.importer import WaternetSnapshotImporter
from ais.models import WaternetSnapshot

log = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        log.info("Starting import")
        for snapshot in WaternetSnapshot.objects.limit_offset_iterator(10):
            WaternetSnapshotImporter(snapshot).start()
        log.info("import Done")
