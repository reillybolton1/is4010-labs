import requests


class WeatherAPI:
    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def _get(self, endpoint, params):
        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}", params=params, timeout=10
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None
        except ValueError:
            return None

    def get_current_weather(self, location):
        params = {"key": self.api_key, "q": location}
        return self._get("current.json", params)

    def get_forecast(self, location, days=3):
        if not isinstance(days, int) or isinstance(days, bool) or not 1 <= days <= 3:
            raise ValueError("days must be between 1 and 3")
        params = {"key": self.api_key, "q": location, "days": days}
        return self._get("forecast.json", params)


def format_current_weather(data):
    loc = data["location"]
    cur = data["current"]
    return f"{loc['name']}, {loc['country']}: {cur['temp_f']}°F, {cur['condition']['text']}"


def format_forecast(data):
    lines = []
    for entry in data["forecast"]["forecastday"]:
        day = entry["day"]
        lines.append(
            f"{entry['date']}: high {day['maxtemp_f']}°F, "
            f"low {day['mintemp_f']}°F, {day['condition']['text']}"
        )
    return "\n".join(lines)