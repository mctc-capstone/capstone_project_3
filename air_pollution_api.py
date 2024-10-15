import requests
import os


def get_air_pollution(coordinates: list) -> int:
    """
    Returns the Air Quality Index for a given set of coordinates from
    OpenWeatherMap's data set.

    Args:
        coords (list): The latitude and longitude (respectively) of a given
            location.

    Returns:
        int: The location's Air Quality Index.

    Raises:
        HTTPError: If the HTTP request was unsuccessful.
    """

    endpoint = "http://api.openweathermap.org/data/2.5/air_pollution"
    payload = {
        "lat": coordinates[0],
        "lon": coordinates[1],
        "appid": os.environ["OWM_API_KEY"],
    }

    response = requests.get(endpoint, params=payload)

    # will raise an HTTPError if the request was unsuccessful
    response.raise_for_status()

    return response.json()["list"][0]["main"]["aqi"]
