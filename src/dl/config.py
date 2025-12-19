import json
import os
import pathlib

# Define the path to the config file
CONFIG_DIR = pathlib.Path.home() / ".config" / "dl"
CONFIG_FILE = CONFIG_DIR / "config.json"

# Default configuration values
DEFAULT_CONFIG = {
    "DOWNLOADS_DIR": str(pathlib.Path.home() / "Downloads"),
    "CATEGORIES": {
        "apks": ["apk"],
        "archives": ["zip", "rar", "7z", "tar", "gz", "iso"],
        "media": ["mp4", "mkv", "avi", "flv", "mov"],
        "music": ["mp3", "flac", "wav", "ogg"],
    },
    "ARIA2_HOST": "http://localhost",
    "ARIA2_PORT": 6800,
    "ARIA2_SECRET": "",
    "UPDATE_INTERVAL": 0.5,
}


def load_config():
    """Loads configuration from JSON file, creating it if it doesn't exist."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    if not CONFIG_FILE.is_file():
        with open(CONFIG_FILE, "w") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG

    with open(CONFIG_FILE, "r") as f:
        user_config = json.load(f)

    # Merge default and user configs, with user values taking precedence
    config = DEFAULT_CONFIG.copy()
    config.update(user_config)
    return config


# Load configuration
_config = load_config()

# Set configuration variables
DOWNLOADS_DIR = _config.get("DOWNLOADS_DIR")
CATEGORIES = _config.get("CATEGORIES")
ARIA2_HOST = _config.get("ARIA2_HOST")
ARIA2_PORT = _config.get("ARIA2_PORT")
UPDATE_INTERVAL = _config.get("UPDATE_INTERVAL")

# Special handling for ARIA2_SECRET: env var can override config file
ARIA2_SECRET = os.environ.get("ARIA2_SECRET", _config.get("ARIA2_SECRET"))

for category in CATEGORIES:
    (pathlib.Path(DOWNLOADS_DIR) / category).mkdir(parents=True, exist_ok=True)
(pathlib.Path(DOWNLOADS_DIR) / "misc").mkdir(parents=True, exist_ok=True)
