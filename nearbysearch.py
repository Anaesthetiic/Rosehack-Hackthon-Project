import requests

def get_county_from_city(api_key, city):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    # Construct the request parameters
    params = {
        "address": city,
        "key": api_key,
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    results = response.json().get("results", [])

    # Extract the county name from the results
    for result in results:
        for component in result.get("address_components", []):
            if "administrative_area_level_2" in component.get("types", []):
                return component.get("long_name")

    return None

def get_counties_nearby(api_key, location, radius):
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    # Construct the request parameters
    params = {
        "location": location,  # Format: "latitude,longitude"
        "radius": radius,
        "type": "locality",
        "key": api_key,
    }

    # Make the API request
    response = requests.get(base_url, params=params)
    results = response.json().get("results", [])

    # Get the county name for each city
    for result in results:
        city = result.get("name")
        county = get_county_from_city(api_key, city)
        result["county"] = county

    return results

def main():
    # Replace with your actual API key
    api_key = 'AIzaSyBdEluVk5_sp43-7fz8iUOw4qdpIKzzytQ'
    location = '33.9806,-117.3755'  # Riverside, CA
    radius = '40233.6'  # 25 miles in meters

    results = get_counties_nearby(api_key, location, radius)
    
    # Print only the county names
    for result in results:
        print(result.get('county'))

if __name__ == "__main__":
    main()