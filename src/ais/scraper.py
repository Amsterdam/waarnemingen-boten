from django.conf import settings
from snapshot.scraper import BaseAPISnapshotScraper

from ais.models import WaternetSnapshot

# API parameters. left, top, right, bottom is bounding box. age is last seen
PARAMS = {'left': 4, 'top': 55, 'right': 8, 'bottom': 50, 'age': 10}


class MissingEnvVariables(Exception):
    """API username or password not found in env variables"""


class InvalidCredentials(Exception):
    """Could not authenticate with provided credentials"""


class EmptyResponse(Exception):
    """Received empty response"""


class WaternetScraper(BaseAPISnapshotScraper):
    url = 'https://waternet.globalguidesystems.com/api/v0/object'
    model = WaternetSnapshot

    def __init__(self):
        super().__init__()
        self.auth_url = 'https://waternet.globalguidesystems.com/api/v0/auth/login'
        self.params = PARAMS

    def get_credentials(self):
        """Retrieve api Credentials"""
        credentials = {
            'userName': settings.WATERNET_USERNAME,
            'password': settings.WATERNET_PASSWORD
        }
        if not all(credentials.values()):
            raise MissingEnvVariables
        return credentials

    def parse(self, response):
        """
        If response is empty an error is raised to avoid
        smearing the db.
        """
        data = response.json()
        if not data:
            raise EmptyResponse()
        return data

    def authenticate(self):
        """Send authentication request and add token to headers"""
        response = self.requests.post(self.auth_url, self.get_credentials())

        if response.status_code != 200:
            raise InvalidCredentials

        token = response.json().get('token')
        auth_header = {'Authorization': f'Bearer {token}'}
        self.headers.update(auth_header)
