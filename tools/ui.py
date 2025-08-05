
import os

from tools.discord import send_webhook_notification
from tools.logs import log
from tools.debug import dprint, retry
from tools.json import save_config, load_config

tree = {
    "0": "Discord Webhook Manager - Tamino1230",
    "1": "Send Webhook Message",
    "2": "View Logs",
    "3": "Edit Configuration",
    "4": "Exit"
}

def menu(config=None):
    log("Menu accessed", "Info", "User is accessing the Discord Webhook Manager menu.")
    dprint("Menu accessed, displaying options to the user.", 1)
    if config is None:
        log("No configuration loaded", "Error", "Default configuration will be used.")
        dprint("No configuration provided, using default settings.", 2)
        return
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        check_link = config.get("webhook_link", "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token")
        if check_link:
            if check_link == "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token":
                print("!!! Webhook URL is not set. Please edit the configuration. !!!")
                log("Webhook URL is not set", "Warning", "Default webhook URL is being used, please update it.")
                dprint("Webhook URL is not set, prompting user to edit configuration.", 2)
            
        for key, value in tree.items():
            if key == "0":
                print(value)
                continue
            print(f"{key}. {value}")

        choice = input(f"Please select an option (1-{len(tree) - 1}): ")
        if choice not in tree:
            print("Invalid choice, please try again.")
            continue
        if choice == '1':
            verify_send_screen(config)
        elif choice == '2':
            view_logs()
        elif choice == '3':
            edit_configuration(config)
        elif choice == '4':
            print("Exiting the Discord Webhook Manager. Goodbye!")
            break

def verify_send_screen(config=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    log("Verify send screen accessed", "Info", "User is verifying the send webhook message screen.")
    dprint("Verify send screen accessed, preparing to send webhook message.", 1)
    if config is None:
        log("No configuration provided", "Error", "Default configuration will be used for sending webhook message.")
        dprint("No configuration provided, using default settings.", 2)
        return
    log("Displaying webhook message preview", "Info", "User is prompted to confirm sending the webhook message.")
    print("Preview:")
    print(f"Webhook URL: {config.get('webhook_link', '[not set]')}")
    if config.get("embed_enabled", False):
        print("Embed:")
        print(f"  Title: {config.get('embed_title', '')}")
        print(f"  Description: {config.get('embed_description', '')}")
        print(f"  Color: {config.get('embed_color', '')}")
        print(f"  Thumbnail: {config.get('embed_thumbnail', '')}")
        print(f"  Footer: {config.get('embed_footer', '')}")
    else:
        print("Embed: Disabled")
        print(f"Content: {config.get('embed_description', 'Default description')}")
    print(f"Max Retries: {config.get('max_retries', 1)}")
    print("\nDo you want to send a webhook message? (yes/no) | default: no)")
    choice = input("> ")
    if choice.lower() == "yes":
        print("Sending webhook message...")
        log("User confirmed to send webhook message", "Info", "Proceeding to send the webhook notification.")
        if retry(lambda: send_webhook_notification(config), retries=config.get("max_retries", 3)):
            log("Webhook message sent successfully", "Success", "Webhook message has been sent based on the provided configuration.")
            dprint("Webhook message sent successfully.", 1)
            print("Webhook message sent successfully.")
    else:
        print("Webhook message not sent.")
        log("User declined to send webhook message", "Info", "Webhook message sending was cancelled by the user.")
        dprint("Webhook message sending was cancelled by the user.", 2)

    input("\nPress Enter to return to the menu...")

def view_logs():
    log("View logs accessed", "Info", "User is viewing the logs of the Discord Webhook Manager.")
    dprint("View logs accessed, displaying log file content.", 1)
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        with open("logs/log.log", "r") as log_file:
            print(log_file.read())
    except FileNotFoundError:
        print("Log file not found. Please ensure the log file exists in: ./logs/log.log")
        log("Log file not found", "Error", "The log file could not be located.")
        dprint("Log file not found, please check the logs directory.", 2)
    input("\nPress Enter to return to the menu...")

def edit_configuration(config):
    os.system('cls' if os.name == 'nt' else 'clear')
    log("Edit configuration accessed", "Info", "User is editing the configuration.")
    dprint("Edit configuration accessed, displaying editable fields.", 1)
    print("Edit Configuration:")
    editable_keys = [
        key for key in config.keys()
        if key not in ["log_file_path", "webhook_link_fake"]
    ]
    for idx, key in enumerate(editable_keys, 1):
        print(f"{idx}. {key}: {config[key]}")
    print(f"{len(editable_keys)+1}. Cancel")
    try:
        choice = int(input(f"Select a field to edit (1-{len(editable_keys)+1}): "))
    except ValueError:
        print("Invalid input. Returning to menu.")
        input("\nPress Enter to return to the menu...")
        return
    if choice == len(editable_keys)+1:
        print("Edit cancelled.")
        input("\nPress Enter to return to the menu...")
        return
    if 1 <= choice <= len(editable_keys):
        key = editable_keys[choice-1]
        current_value = config[key]
        new_value = input(f"Enter new value for '{key}' (current: {current_value}): ")
        # Type conversion for bool/int fields
        if isinstance(current_value, bool):
            new_value = new_value.lower() in ("true", "1", "yes", "y")
        elif isinstance(current_value, int):
            try:
                new_value = int(new_value)
            except ValueError:
                print("Invalid integer. No changes made.")
                input("\nPress Enter to return to the menu...")
                return
        config[key] = new_value
        save_config("config/default_config.json", config)
        print(f"'{key}' updated and configuration saved.")
        log(f"Config field '{key}' updated", "Success", f"New value: {new_value}")
    else:
        print("Invalid selection.")
    input("\nPress Enter to return to the menu...")