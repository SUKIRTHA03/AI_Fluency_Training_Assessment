import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        temperature = data["current_condition"][0]["temp_C"]

        return f"Current temperature in {city}: {temperature}°C"

    except Exception as e:
        return f"Weather tool failed: {e}"