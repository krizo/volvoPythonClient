from api.vehicle import Vehicle


def test_vehicle_list():
    vehicle_list = Vehicle.get_vehicle_list()
    assert vehicle_list, "Vehicle list doesn't return anything"
    assert vehicle_list.get('vehicles'), "No vehicles key in the response"
    assert isinstance(vehicle_list.get('vehicles'), dict), "Vehicle list response is not a list"
    assert len(vehicle_list.get('vehicles')) > 0, "Vehicle list is empty"
