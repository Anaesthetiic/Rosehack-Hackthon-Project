import requests
import time
import random

def get_places_nearby(api_key, location, radius):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "location": location,
        "radius": radius,
        "key": api_key,
    }

    places = []
    while True:
        response = requests.get(base_url, params=params)
        data = response.json()
        results = data.get("results", [])

        for result in results:
            places.append(result["name"])

        # If there's a next page token, use it to get the next set of results
        next_page_token = data.get("next_page_token")
        if next_page_token:
            # Must wait before sending the request with the next page token
            time.sleep(2)
            params["pagetoken"] = next_page_token
        else:
            break

    return places

def main():
    # Replace with your actual API key
    api_key = 'AIzaSyBdEluVk5_sp43-7fz8iUOw4qdpIKzzytQ'
    location = '33.9806,-117.3755'  # Riverside, CA
    radius = '32186.9'  # 20 miles in meters

    places = get_places_nearby(api_key, location, radius)
    
    # Select 5 random places
    places = random.sample(places, 5)

    # Print the place names
    for place in places:
        print(place)

if __name__ == "__main__":
    main()