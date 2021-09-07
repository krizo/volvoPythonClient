import yaml


class Credentials:
    _credentials_file = 'secrets.yml'
    _credentials = None

    @classmethod
    def _get_credentials(cls) -> dict:
        if cls._credentials is None:
            with open(cls._credentials_file, 'r') as stream:
                cls._credentials = yaml.safe_load(stream)
        return cls._credentials

    @classmethod
    def get_user_access_token(cls) -> str:
        return cls._get_credentials().get('user_access_token')

    @classmethod
    def get_vcc_api_key_primary(cls) -> str:
        return cls._get_credentials().get('vcc_api_key_primary')

    @classmethod
    def get_vcc_api_key_secondary(cls) -> str:
        return cls._get_credentials().get('vcc_api_key_secondary')
