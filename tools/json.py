
import json
import os

from tools.logs import log
from tools.debug import dprint

CONFIG_FILE_PATH = "config/default_config.json"

default_data = {
    "webhook_link": "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token",
    "embed_enabled": True,
    "embed_title": "Title text here",
    "embed_description": "This is a default notification message.",
    "embed_color": "0x00ff00",
    "embed_thumbnail": "https://example.com/thumbnail.png",
    "embed_footer": "Footer text here",
    "max_retries": 3
}

def load_config(file_path):
    dprint(f"Loading configuration from {file_path}", 1)
    os.mkdir(os.path.dirname(file_path)) if not os.path.exists(os.path.dirname(file_path)) else None
    #* if not exists, make new config file
    if not os.path.exists(file_path):
        log("Configuration file not found", "Warning", f"Creating default configuration at {file_path}.")
        dprint(f"Configuration file not found at {file_path}. Making new default config file.", 2)
        with open(file_path, 'w') as f:
            json.dump(default_data, f, indent=4)
            dprint("Default configuration file created.", 2)
            log("Default configuration created", "Info", "Using default configuration values.")
            return default_data
    with open(file_path, 'r') as f:
        dprint(f"Configuration file {file_path} loaded successfully.", 1)
        log("Configuration file loaded", "Info", f"Configuration loaded from {file_path}.")
        return json.load(f)

def save_config(file_path, config):
    os.mkdir(os.path.dirname(file_path)) if not os.path.exists(os.path.dirname(file_path)) else None
    dprint(f"Saving configuration to {file_path}", 1)
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)
    dprint(f"Configuration saved to {file_path}", 1)
    log("Configuration saved", "Info", f"Configuration saved to {file_path}.")
