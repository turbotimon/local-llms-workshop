import requests


def get_temperature(city: str) -> float:
    geo = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1},
        timeout=10,
    )
    geo.raise_for_status()
    place = geo.json()["results"][0]

    forecast = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={"latitude": place["latitude"], "longitude": place["longitude"], "current": "temperature_2m"},
        timeout=10,
    )
    forecast.raise_for_status()
    return forecast.json()["current"]["temperature_2m"]


if __name__ == "__main__":
    print(get_temperature("Rapperswil"))
