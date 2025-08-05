
import datetime
import os
# from tools.debug import dprint

LOG_FILE_PATH = "logs/log.log"

def log(action="No action specified", status="Info", details="No details provided"):
    if not os.path.exists(os.path.dirname(LOG_FILE_PATH)):
        os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
    timestamp = datetime.datetime.now().isoformat() 
    with open(LOG_FILE_PATH, "a") as log_file:
        log_file.write(f"[{timestamp:<23}] Action: {action:<41}, Status: {status:<11}, Details: {details:<19}\n")
        # dprint(f"[{timestamp:<23}] Action: {action:<41}, Status: {status:<11}, Details: {details:<19}\n")

