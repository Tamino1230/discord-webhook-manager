# Discord Webhook Manager by Tamino1230

A versatile Python-based tool for sending, managing, and configuring Discord webhook messages through a user-friendly command-line interface.

## Overview

This project provides a simple yet powerful way to interact with Discord webhooks. It's designed for users who need to send customized notifications, manage configurations dynamically, and keep track of activities through logging. The tool is operated via a console menu, making it accessible for users of all skill levels.

## Features

- **Interactive Menu**: A simple and intuitive command-line interface to manage all functionalities.
- **Dynamic Configuration**: Edit webhook settings on-the-fly without manually editing JSON files. The configuration is loaded from `config/default_config.json` and can be modified from the UI.
- **Embed & Simple Messages**: Supports both rich embed messages and simple text-based content.
- **Robust Error Handling**: Implements a retry mechanism for sending webhooks, with configurable retry attempts.
- **Detailed Logging**: Keeps a record of all actions, statuses, and details in `logs/log.log`.
- **Debugging Mode**: An optional debug mode that provides more verbose output for development and troubleshooting.

## Installation & Usage

### Prerequisites

- Python 3.x
- `requests` library

### Steps

1.  **Clone the repository or download the source code.**

2.  **Install dependencies:**
    Open your terminal or command prompt and run:
    ```bash
    pip install requests
    ```

3.  **Run the application:**
    ```bash
    python main.py
    ```
    This will start the application and display the main menu.

## Configuration

The application's behavior is controlled by `config/default_config.json`. If this file is not found, a default one will be created automatically.

### Main Configuration (`config/default_config.json`)

| Key                 | Type    | Description                                                                                             |
| ------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| `webhook_link`      | string  | The URL of the Discord webhook to which messages will be sent.                                          |
| `embed_enabled`     | boolean | If `true`, sends a rich embed message. If `false`, sends a simple text message.                         |
| `embed_title`       | string  | The title of the embed message.                                                                         |
| `embed_description` | string  | The main content/body of the embed message or the content of a simple message.                          |
| `embed_color`       | string  | The hex color code for the embed's side strip (e.g., `"0x00ff00"` for green).                             |
| `embed_thumbnail`   | string  | The URL of an image to display as a thumbnail in the embed.                                             |
| `embed_footer`      | string  | The text to display at the bottom of the embed.                                                         |
| `max_retries`       | integer | The maximum number of times the application will try to send a webhook if it fails.                     |

### Debug Mode

To enable debug mode, create a file named `debug_mode.txt` inside the `config` directory and write `true` in it. This will enable detailed debug messages in the console.

## Menu Options

1.  **Send Webhook Message**: Prompts for confirmation and then sends a message to the configured webhook based on the current settings.
2.  **View Logs**: Displays the contents of the log file (`logs/log.log`).
3.  **Edit Configuration**: Allows you to interactively edit the values in `config/default_config.json`.
4.  **Exit**: Closes the application.

## Logging

All operations, including errors and successes, are logged in `logs/log.log`. Each log entry includes a timestamp, the action performed, a status, and relevant details.

## Project Structure

```
.
├── config/
│   ├── default_config.json   # Main configuration file
│   └── debug_mode.txt        # (Optional) Enables debug mode
├── logs/
│   └── log.log               # Log file
├── tools/
│   ├── discord.py            # Handles sending webhook messages
│   ├── json.py               # Manages loading/saving config
│   ├── logs.py               # Logging utility
│   ├── ui.py                 # Defines the command-line interface
│   └── debug.py              # Debugging utilities
├── main.py                   # Main entry point of the application
└── README.md                 # This file
```

## Author

This project was created by **Tamino1230**.

- **GitHub**: [Tamino1230](https://github.com/tamino1230)
- **Discord**: [Server](https://discord.gg/8b8R9qCBF8)
