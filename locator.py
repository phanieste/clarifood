from googleplaces import GooglePlaces, types

# API_KEY = 'AIzaSyDhcoR-s9nQaVM-Hl3tDYlmjgGfdbho-qc'
API_KEY = 'AIzaSyAT0pUlWNxcVDVDU2BO3Z1c0tlWk_sdRe8'

google_places = GooglePlaces(API_KEY)

def find(query=None, location='New York, NY'):
    result = google_places.text_search(
        query=query, location=location, types=[types.TYPE_FOOD])

    result_list = []
    for place in result.places[:5]:
        place.get_details()
        result_list.append({
            'name': place.name,
            'place_id': place.place_id,
            'address': place.formatted_address,
            'website': place.website,
            'location': place.geo_location
        })

    return result_list
