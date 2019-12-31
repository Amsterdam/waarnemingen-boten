from django.contrib.gis import forms, geos

from ais import constants
from ais.models import Waternet
from ais.constants import WGS84_SRID


class CustomPointField(forms.PointField):
    def to_python(self, value):
        return geos.Point(
            value['x'],
            value['y'],
            srid=WGS84_SRID
        )


class WaternetImporterForm(forms.ModelForm):
    geo_location = CustomPointField()
    lastupdate = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%f%z'])
    lastmoved = forms.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%S.%f%z'], required=False)

    class Meta:
        model = Waternet
        fields = list(constants.WATERNET_RAW_TO_MODEL_MAPPING.values())
