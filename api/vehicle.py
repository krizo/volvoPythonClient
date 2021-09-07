from api.volvo_api_connector import VolvoApiConnector


class Vehicle:
    _client = VolvoApiConnector('vehicles')

    @classmethod
    def get_vehicle_list(cls):
        return cls._client.get()

