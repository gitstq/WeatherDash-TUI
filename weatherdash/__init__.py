#!/usr/bin/env python3
"""
WeatherDash-TUI: A beautiful terminal weather dashboard
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import httpx
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Button
from textual.reactive import reactive
from textual import events

# Weather API endpoints
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

# ASCII Weather Icons
WEATHER_ICONS = {
    "clear_day": """
      \\   |   //
        \\     //
          \\ //
       \\     //
    \\   \\   //   /
      \\  |  //  /
        \\ | // /
     ========O========
        // | \\ \\
      //  |  \\  \\
    //   //   \\   \\
          // \\
        //     \\
      //   |   \\
""",
    "clear_night": """
       .--------.
      /   .--.   \\
     |  /    \\   |
     |  \\    /   |
      \\   '--'   /
       '--------'
        __  __
       /  \\/  \\
       \\      /
        '----'
""",
    "cloudy": """
         \\   |   //
           \\   //
             \\//
           .-~~~-.
          /       \\
         |  \\ | //  |
         |   \\|//   |
          \\   ||   /
           '-----'
        //   |   \\
""",
    "rain": """
       .-~~~-.
      /       \\
     |         |
     |         |
      \\       /
       '-----'
      | | | |
      | | | |
      | | | |
""",
    "snow": """
       .-~~~-.
      /       \\
     |         |
     |         |
      \\       /
       '-----'
      * * * *
     * * * * *
      * * * *
""",
    "thunderstorm": """
       .-~~~-.
      /       \\
     |         |
     |    /_\\  |
      \\  /_\\  /
       '-----'
      | | | |
      | | | |
     /_\\| | /_\\
""",
    "fog": """
    ~~~~~~~~~~~~~
   ~~~~~~~~~~~~~~~
  ~~~~~~~~~~~~~~~~
   ~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~
   ~~~~~~~~~~~~~~~
  ~~~~~~~~~~~~~~~~
   ~~~~~~~~~~~~~~~
""",
}

# Small emoji icons
WEATHER_EMOJI = {
    0: ("☀️", "Clear sky"),
    1: ("🌤️", "Mainly clear"),
    2: ("⛅", "Partly cloudy"),
    3: ("☁️", "Overcast"),
    45: ("🌫️", "Foggy"),
    48: ("🌫️", "Depositing rime fog"),
    51: ("🌧️", "Light drizzle"),
    53: ("🌧️", "Moderate drizzle"),
    55: ("🌧️", "Dense drizzle"),
    61: ("🌧️", "Slight rain"),
    63: ("🌧️", "Moderate rain"),
    65: ("🌧️", "Heavy rain"),
    71: ("🌨️", "Slight snow"),
    73: ("🌨️", "Moderate snow"),
    75: ("🌨️", "Heavy snow"),
    95: ("⛈️", "Thunderstorm"),
}

WIND_DIRECTIONS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                   "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]


class WeatherClient:
    """Weather API client using Open-Meteo (free, no API key required)"""
    
    def __init__(self):
        self.client = httpx.Client(timeout=10.0)
    
    def geocode(self, city: str) -> Optional[dict]:
        """Get coordinates for a city"""
        try:
            response = self.client.get(
                GEOCODING_URL,
                params={"name": city, "count": 1, "language": "en", "format": "json"}
            )
            data = response.json()
            if data.get("results"):
                return data["results"][0]
        except Exception as e:
            print(f"Geocoding error: {e}")
        return None
    
    def get_weather(self, city: str) -> Optional[dict]:
        """Get weather data for a city"""
        geo = self.geocode(city)
        if not geo:
            return None
        
        try:
            response = self.client.get(
                WEATHER_URL,
                params={
                    "latitude": geo["latitude"],
                    "longitude": geo["longitude"],
                    "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,wind_direction_10m,surface_pressure,is_day",
                    "daily": "temperature_2m_max,temperature_2m_min,weather_code",
                    "timezone": "auto",
                    "forecast_days": 7
                }
            )
            data = response.json()
            
            # Combine with location info
            result = {
                "city": geo["name"],
                "country": geo.get("country", ""),
                "current": data.get("current", {}),
                "daily": data.get("daily", {}),
                "timestamp": datetime.now().isoformat()
            }
            return result
        except Exception as e:
            print(f"Weather API error: {e}")
        return None


class Cache:
    """Simple file-based cache for weather data and favorites"""
    
    def __init__(self):
        self.cache_dir = Path.home() / ".cache" / "weatherdash-tui"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.cache_file = self.cache_dir / "cache.json"
        self.favorites_file = self.cache_dir / "favorites.json"
    
    def save_weather(self, city: str, data: dict):
        """Save weather data to cache"""
        cache = self._load_cache()
        cache[city.lower()] = {
            "data": data,
            "timestamp": datetime.now().timestamp()
        }
        self._save_cache(cache)
    
    def get_weather(self, city: str) -> Optional[dict]:
        """Get cached weather data (valid for 30 minutes)"""
        cache = self._load_cache()
        entry = cache.get(city.lower())
        if entry:
            # Cache valid for 30 minutes
            if datetime.now().timestamp() - entry["timestamp"] < 1800:
                return entry["data"]
        return None
    
    def _load_cache(self) -> dict:
        if self.cache_file.exists():
            try:
                return json.loads(self.cache_file.read_text())
            except:
                pass
        return {}
    
    def _save_cache(self, cache: dict):
        self.cache_file.write_text(json.dumps(cache, indent=2))
    
    def get_favorites(self) -> list:
        """Get list of favorite cities"""
        if self.favorites_file.exists():
            try:
                return json.loads(self.favorites_file.read_text())
            except:
                pass
        return ["Beijing", "Shanghai", "Shenzhen"]
    
    def add_favorite(self, city: str):
        """Add city to favorites"""
        favorites = self.get_favorites()
        if city.lower() not in [c.lower() for c in favorites]:
            favorites.append(city)
            self.favorites_file.write_text(json.dumps(favorites, indent=2))
    
    def remove_favorite(self, city: str):
        """Remove city from favorites"""
        favorites = [c for c in self.get_favorites() if c.lower() != city.lower()]
        self.favorites_file.write_text(json.dumps(favorites, indent=2))


class WeatherWidget(Static):
    """Widget to display weather information"""
    
    weather_data = reactive(None)
    show_ascii = reactive(True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = WeatherClient()
        self.cache = Cache()
    
    def update_weather(self, city: str, offline: bool = False):
        """Update weather data for a city"""
        # Try cache first
        data = self.cache.get_weather(city)
        
        if not data and not offline:
            data = self.client.get_weather(city)
            if data:
                self.cache.save_weather(city, data)
        
        self.weather_data = data
    
    def render(self) -> Panel:
        if not self.weather_data:
            return Panel("Loading weather data...", title="Weather")
        
        data = self.weather_data
        current = data.get("current", {})
        city = data.get("city", "Unknown")
        country = data.get("country", "")
        
        # Get weather info
        temp = current.get("temperature_2m", 0)
        humidity = current.get("relative_humidity_2m", 0)
        wind_speed = current.get("wind_speed_10m", 0)
        wind_dir = current.get("wind_direction_10m", 0)
        pressure = current.get("surface_pressure", 0)
        weather_code = current.get("weather_code", 0)
        is_day = current.get("is_day", 1) == 1
        
        # Get icon and description
        emoji, description = WEATHER_EMOJI.get(weather_code, ("❓", "Unknown"))
        
        # Wind direction
        dir_idx = int((wind_dir + 11.25) / 22.5) % 16
        wind_direction = WIND_DIRECTIONS[dir_idx]
        
        # Build content
        lines = []
        
        # ASCII icon or emoji
        if self.show_ascii:
            if weather_code == 0:
                icon = WEATHER_ICONS["clear_day" if is_day else "clear_night"]
            elif weather_code in [1, 2, 3]:
                icon = WEATHER_ICONS["cloudy"]
            elif weather_code in [61, 63, 65, 51, 53, 55]:
                icon = WEATHER_ICONS["rain"]
            elif weather_code in [71, 73, 75]:
                icon = WEATHER_ICONS["snow"]
            elif weather_code == 95:
                icon = WEATHER_ICONS["thunderstorm"]
            elif weather_code in [45, 48]:
                icon = WEATHER_ICONS["fog"]
            else:
                icon = WEATHER_ICONS["cloudy"]
            
            lines.append(f"[yellow]{icon}[/]")
        else:
            lines.append(f"\n[yellow]{emoji}[/]\n")
        
        lines.append("")
        lines.append(f"[bold cyan]📍 {city}, {country}[/]")
        lines.append(f"[bold white]🌡️ Temperature: {temp}°C[/]")
        lines.append(f"[blue]💧 Humidity: {humidity}%[/]")
        lines.append(f"[green]💨 Wind: {wind_speed} km/h {wind_direction}[/]")
        lines.append(f"[magenta]🌡️ Pressure: {pressure:.0f} hPa[/]")
        lines.append(f"[yellow]☁️ {description}[/]")
        
        return Panel("\n".join(lines), title=f"Weather - {city}", border_style="cyan")


class WeatherApp(App):
    """Main TUI Application"""
    
    CSS = """
    Screen {
        layout: vertical;
    }
    
    .weather-container {
        height: 100%;
        align: center middle;
    }
    
    .weather-widget {
        width: 80%;
        height: auto;
    }
    
    .footer-bar {
        dock: bottom;
        height: 3;
        background: $panel;
    }
    """
    
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("r", "refresh", "Refresh"),
        ("n", "next_city", "Next City"),
        ("p", "prev_city", "Prev City"),
        ("a", "toggle_ascii", "Toggle ASCII"),
        ("h", "toggle_help", "Help"),
    ]
    
    current_city = reactive("Beijing")
    city_index = reactive(0)
    
    def __init__(self, city: Optional[str] = None, offline: bool = False):
        super().__init__()
        self.cache = Cache()
        self.favorites = self.cache.get_favorites()
        self.offline = offline
        if city:
            self.current_city = city
        elif self.favorites:
            self.current_city = self.favorites[0]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            WeatherWidget(classes="weather-widget"),
            classes="weather-container"
        )
        yield Footer()
    
    def on_mount(self):
        """Load initial weather data"""
        self._update_weather()
    
    def _update_weather(self):
        """Update weather widget"""
        widget = self.query_one(WeatherWidget)
        widget.update_weather(self.current_city, self.offline)
    
    def action_refresh(self):
        """Refresh weather data"""
        self._update_weather()
    
    def action_next_city(self):
        """Switch to next city in favorites"""
        if self.favorites:
            self.city_index = (self.city_index + 1) % len(self.favorites)
            self.current_city = self.favorites[self.city_index]
            self._update_weather()
    
    def action_prev_city(self):
        """Switch to previous city in favorites"""
        if self.favorites:
            self.city_index = (self.city_index - 1) % len(self.favorites)
            self.current_city = self.favorites[self.city_index]
            self._update_weather()
    
    def action_toggle_ascii(self):
        """Toggle ASCII art mode"""
        widget = self.query_one(WeatherWidget)
        widget.show_ascii = not widget.show_ascii
        widget.refresh()


def main():
    """CLI entry point"""
    parser = argparse.ArgumentParser(
        description="WeatherDash-TUI: A beautiful terminal weather dashboard"
    )
    parser.add_argument("-c", "--city", help="City name to display weather for")
    parser.add_argument("--refresh", type=int, default=300, help="Refresh interval in seconds")
    parser.add_argument("--offline", action="store_true", help="Use offline cached data")
    parser.add_argument("--add", metavar="CITY", help="Add city to favorites")
    parser.add_argument("--remove", metavar="CITY", help="Remove city from favorites")
    parser.add_argument("-l", "--list", action="store_true", help="List favorite cities")
    
    args = parser.parse_args()
    
    cache = Cache()
    
    # Handle non-TUI commands
    if args.list:
        favorites = cache.get_favorites()
        print("📍 Favorite Cities:")
        for i, city in enumerate(favorites, 1):
            print(f"  {i}. {city}")
        return
    
    if args.add:
        cache.add_favorite(args.add)
        print(f"✅ Added '{args.add}' to favorites")
        return
    
    if args.remove:
        cache.remove_favorite(args.remove)
        print(f"❌ Removed '{args.remove}' from favorites")
        return
    
    # Run TUI app
    app = WeatherApp(city=args.city, offline=args.offline)
    app.run()


if __name__ == "__main__":
    main()
