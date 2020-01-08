from django.contrib.gis.db import models
from snapshot.models import BaseSnapshot

from ais.constants import WGS84_SRID
from ais.managers import WaternetSnapshotManager


class WaternetSnapshot(BaseSnapshot):
    objects = WaternetSnapshotManager()


class Waternet(models.Model):
    mmsi = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)
    type = models.IntegerField(null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    geo_location = models.PointField(name='geo_location', srid=WGS84_SRID)
    speed = models.IntegerField()
    direction = models.IntegerField()
    status = models.IntegerField()
    sensor = models.CharField(max_length=255)
    lastupdate = models.DateTimeField()
    lastmoved = models.DateTimeField(null=True, blank=True)

    scraped_at = models.DateTimeField()

    class Meta:
        ordering = ('scraped_at',)
