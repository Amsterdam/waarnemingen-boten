import logging

from snapshot.base_importer import BaseImportFactory, BaseSnapshotImporter
from ais import constants
from ais.forms import WaternetImporterForm
from ais.models import Waternet

log = logging.getLogger(__name__)


class WaternetImportFactory(BaseImportFactory):
    raw_to_model_fields = constants.WATERNET_RAW_TO_MODEL_MAPPING
    model_form = WaternetImporterForm
    areas_fields = {
        'neighbourhood_field': 'buurt_code',
        'district_field': 'stadsdeel',
        'geometry_field': 'geo_location'
    }


class WaternetSnapshotImporter(BaseSnapshotImporter):
    import_factory = WaternetImportFactory
    import_model = Waternet
