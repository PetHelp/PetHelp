def resolve_geo_for_user(user_instance):
    coords = get_geo_coordinates_for_address(user_instance.address)
    user_instance.address_lat = coords["lat"]
    user_instance.address_lng = coords["lng"]
    user_instance.save()
    return user_instance


def resolve_geo_for_animal(animal_instance):
    coords = get_geo_coordinates_for_address(animal_instance.current_address)
    animal_instance.current_address_lat = coords["lat"]
    animal_instance.current_address_lng = coords["lng"]
    animal_instance.save()
    return animal_instance


def get_geo_coordinates_for_address(address_string):
    if not address_string:
        return dict(lat=None, lng=None)
    # TODO: add geocoding api call here
    return dict(lat=None, lng=None)
