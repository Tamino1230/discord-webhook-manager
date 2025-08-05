
import discord
import requests
import json
import time

from tools.logs import log
from tools.debug import dprint

def create_embed_payload(config: dict) -> dict:
    return {
        "embeds": [
            {
                "title": config.get("embed_title", "Default Title"),
                "description": config.get("embed_description", "Default description"),
                "color": int(config.get("embed_color", 0x00ff00), 16),
                "thumbnail": {
                    "url": config.get("embed_thumbnail", "None")
                },
                "footer": {
                    "text": config.get("embed_footer", "Default footer text")
                }
            }
        ]
    }

def create_content_payload(config: dict) -> dict:
    return {
        "content": config.get("embed_description", "Default description")
    }

def send_webhook_notification(config: dict) -> bool:
    webhook_url = config.get("webhook_link", None)
    #* If webhook URL is not set
    if not webhook_url:
        log("Webhook URL is not set", "Error", "No webhook URL provided in the configuration.")
        print("Webhook URL is not set in the configuration.")
        dprint("Webhook URL is not set, cannot send notification.", 3)
        return False
    
    #* Prepare the payload
    if config.get("embed_enabled", False):
        payload = create_embed_payload(config)
    else:
        payload = create_content_payload(config)

    #* Send the Payload
    status = requests.post(webhook_url, json=payload)
    if status.status_code == 204:
        log("Webhook notification sent successfully", "Success", f"Payload: {json.dumps(payload)}")
        return True
    elif status.status_code == 429:
        print("Rate limit hit, retrying after delay...")
        log("Rate limit hit, retrying after delay", "Warning", f"Retry after {status.json().get('retry_after', 1)} seconds.")
        dprint(f"Rate limit hit, retrying after delay", 2)
        time.sleep(5)
        return False
    elif status.status_code == 400:
        log("Bad request to webhook", "Error", f"Payload: {json.dumps(payload)}, Response: {status.text}")
        print("Bad request to webhook, check your configuration. (Most likely Webhook doesn't exist.)")
        dprint("Bad request to webhook, check your configuration. (Most likely Webhook doesn't exist.)", 2)
        return False
    else:
        log("Failed to send webhook notification", "Error", f"Status code: {status.status_code}, Response: {status.text}")
        return False
