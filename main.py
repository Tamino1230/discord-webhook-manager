
from tools.json import load_config, save_config
from tools.logs import log
from tools.discord import send_webhook_notification
from tools.debug import dprint, retry
from tools.ui import menu

CONFIG_FILE_PATH = "config/default_config.json"
config = load_config(CONFIG_FILE_PATH)

def update_config(new_values):
    config.update(new_values)
    save_config(CONFIG_FILE_PATH, new_values)

if __name__ == "__main__":
    # log("Starting the webhook notification process", "Info", "Loading configuration and preparing to send notifications.")
    # if retry(lambda: send_webhook_notification(config), retries=config.get("max_retries", 3)):
    #     log("Webhook notification process completed", "Info", "Notifications sent based on the provided configuration.")
    # else:
    #     log("Webhook notification process failed", "Error", "There was an issue sending the notifications.")
    menu(config)