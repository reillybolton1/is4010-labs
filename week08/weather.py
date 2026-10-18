import argparse
import os
import sys

try:  # imported as a package (tests: from week08 import weather)
    from .favorites import FavoritesManager
    from .weather_api import WeatherAPI, format_current_weather, format_forecast
except ImportError:  # run as a script (python week08/weather.py)
    from favorites import FavoritesManager
    from weather_api import WeatherAPI, format_current_weather, format_forecast

FAVORITES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "favorites.json")


def load_api_key():
    """Return the key from WEATHER_API_KEY, else from config.py, else None."""
    key = os.environ.get("WEATHER_API_KEY")
    if key:
        return key
    try:
        from . import config
    except ImportError:
        try:
            import config
        except ImportError:
            return None
    for attr in ("WEATHER_API_KEY", "API_KEY"):
        value = getattr(config, attr, None)
        if value:
            return value
    return None


def build_parser():
    parser = argparse.ArgumentParser(description="Weather command-line tool")
    sub = parser.add_subparsers(dest="command", required=True)

    current = sub.add_parser("current", help="show current weather")
    current.add_argument("location")

    forecast = sub.add_parser("forecast", help="show a forecast")
    forecast.add_argument("location")
    forecast.add_argument("--days", type=int, default=3)

    fav = sub.add_parser("favorites", help="manage favorite locations")
    fav_sub = fav.add_subparsers(dest="favorites_command", required=True)
    add = fav_sub.add_parser("add")
    add.add_argument("name")
    add.add_argument("location")
    fav_sub.add_parser("list")
    remove = fav_sub.add_parser("remove")
    remove.add_argument("name")
    return parser


def _error(message):
    print(message, file=sys.stderr)
    return 1


def _handle_favorites(args, favorites):
    if args.favorites_command == "add":
        if not favorites.add(args.name, args.location):
            return _error(f"Error: favorite '{args.name}' already exists")
        print(f"Added favorite {args.name}: {args.location}")
    elif args.favorites_command == "remove":
        if not favorites.remove(args.name):
            return _error(f"Error: favorite '{args.name}' not found")
        print(f"Removed favorite {args.name}")
    else:
        items = favorites.list_all()
        if not items:
            print("No favorites saved.")
        for name, location in items.items():
            print(f"{name}: {location}")
    return 0


def main(argv=None):
    args = build_parser().parse_args(argv)
    favorites = FavoritesManager(FAVORITES_FILE)

    if args.command == "favorites":
        return _handle_favorites(args, favorites)

    api_key = load_api_key()
    if not api_key:
        return _error("Error: no API key found. Set WEATHER_API_KEY or add it to config.py")

    location = favorites.get_location(args.location) or args.location
    api = WeatherAPI(api_key)

    if args.command == "current":
        data = api.get_current_weather(location)
        formatter = format_current_weather
    else:
        try:
            data = api.get_forecast(location, args.days)
        except ValueError as exc:
            return _error(f"Error: {exc}")
        formatter = format_forecast

    if data is None:
        return _error("Error: could not retrieve weather data")
    try:
        print(formatter(data))
    except (KeyError, TypeError):
        return _error("Error: unexpected response from weather service")
    return 0


if __name__ == "__main__":
    sys.exit(main())