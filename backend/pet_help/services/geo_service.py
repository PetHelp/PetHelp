import requests
from django.conf import settings
from geopy import distance


def resolve_geo_for_address(instance):
    coords = get_geo_coordinates_for_address(instance.address)
    instance.address_lat = coords["lat"]
    instance.address_lng = coords["lng"]
    instance.save()
    return instance


"""
def get_geo_coordinates_for_address(address_string):
    if not address_string:
        return dict(lat=None, lng=None)
    url = "{}?key={}".format(settings.MAP_QUEST_GEOCODING_URL, settings.MAP_QUEST_API_KEY)
    try:
        response = requests.post(url, dict(location=address_string))
        if response.status_code == 200:
            return response.json()["results"][0]["locations"][0]["displayLatLng"]
    except Exception as e:
        # FIXME: handle error properly
        pass
    return dict(lat=None, lng=None)
"""


def get_geo_coordinates_for_address(address_string):
    if not address_string:
        return dict(lat=None, lng=None)
    try:
        params = {"q": address_string, "format": "json"}
        response = requests.get(settings.OSM_GEOCODING_URL, params=params)
        response_json = response.json()[0]
        latitude = response_json["lat"]
        longitude = response_json["lon"]
        return dict(lat=latitude, lng=longitude)

    except Exception as e:
        # FIXME: handle errors properly
        pass

    return dict(lat=None, lng=None)


def get_distance_between_points_in_km(lat1, lng1, lat2, lng2):
    return distance.distance((lat1, lng1), (lat2, lng2)).km
