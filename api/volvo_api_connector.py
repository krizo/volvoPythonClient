import requests
import vcr
from pip._internal.network.utils import raise_for_status
from requests import Response, Session

from credentials import Credentials
from helpers import get_timestamp

cassette_logger = vcr.VCR(
    serializer='yaml',
    cassette_library_dir='../logs/vcr_cassettes',
    record_mode='all',
    match_on=['uri', 'method'],
    filter_headers=['Ocp-Apim-Subscription-Key']
)


class VolvoApiConnector:
    BASE_URI = "https://api.volvocars.com/extended-vehicle/v1/"
    _headers = None
    _credentials: Credentials = None

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.session = Session()

    def get(self) -> Response:
        with cassette_logger.use_cassette(f"get_{self.endpoint}_{get_timestamp()}.yaml"):
            response = self.session.get(url=self.BASE_URI + self.endpoint, headers=self._get_headers())
            if response.ok:
                return response.json()
            raise_for_status(response)

    def _get_headers(self) -> dict:
        if not self._headers:
            self._credentials = Credentials()
            self._headers = {
                'Accept': "application/json",
                'Connection': 'Keep-Alive',
                'authorization': f"Bearer {self._credentials.access_token}",
                'vcc-api-key': self._credentials.api_key_primary
            }
        return self._headers
