from snapshot.managers import BaseSnapshotManager
from ais import models


class BoatTrackingSnapshotManager(BaseSnapshotManager):
    def get_import_model(self):
        return models.BoatTracking
