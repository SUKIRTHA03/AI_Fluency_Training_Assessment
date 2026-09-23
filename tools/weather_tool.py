import requests


def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()

        data = response.json()
        current = data["current_condition"][0]

        return {
            "city": city,
            "temperature_c": current["temp_C"],
            "description": current["weatherDesc"][0]["value"],
            "humidity": current["humidity"]
        }

    except requests.exceptions.Timeout:
        return {
            "city": city,
            "error": "Weather service timed out."
        }

    except requests.exceptions.RequestException as e:
        return {
            "city": city,
            "error": f"Weather service request failed: {e}"
        }

    except (KeyError, IndexError, ValueError):
        return {
            "city": city,
            "error": "Weather service returned an unexpected response."
        }