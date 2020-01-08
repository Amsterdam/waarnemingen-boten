from snapshot.managers import BaseSnapshotManager

from ais import models


class WaternetSnapshotManager(BaseSnapshotManager):
    def get_import_model(self):
        return models.Waternet
