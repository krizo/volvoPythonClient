import yaml

from helpers import get_root_dir


class Credentials:
    _credentials_file = get_root_dir() + 'secrets.yml'
    _credentials = None

    def __init__(self):
        self._credentials = self._get_credentials()

    def _get_credentials(self) -> dict:
        if self._credentials is None:
            with open(self._credentials_file, 'r') as stream:
                self._credentials = yaml.safe_load(stream)
        return self._credentials

    @property
    def access_token(self) -> str:
        return self._get_credentials().get('user_access_token')

    @property
    def api_key_primary(self) -> str:
        return self._get_credentials().get('vcc_api_key_primary')

    @property
    def api_key_secondary(self) -> str:
        return self._get_credentials().get('vcc_api_key_secondary')
