import json
import os


class FavoritesManager:
    """Store favorite locations by case-insensitive name, saved as JSON."""

    def __init__(self, filename):
        self.filename = filename
        self._favorites = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError):
            return {}
        if not isinstance(data, dict):
            return {}
        return {str(k).lower(): v for k, v in data.items()}

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self._favorites, f, indent=4)

    def add(self, name, location):
        """Add a favorite. Return False if the name already exists."""
        key = name.strip().lower()
        if key in self._favorites:
            return False
        self._favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        """Remove a favorite. Return False if the name does not exist."""
        key = name.strip().lower()
        if key not in self._favorites:
            return False
        del self._favorites[key]
        self._save()
        return True

    def list_all(self):
        """Return a copy of all favorites as {name: location}."""
        return dict(self._favorites)

    def get_location(self, name):
        """Return the location for name, or None if it is not saved."""
        return self._favorites.get(name.strip().lower())