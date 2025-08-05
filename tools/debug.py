
from tools.logs import log

DEBUG_ON = True

def dprint(message: str, urgency: int = 3):
    if DEBUG_ON:
        if urgency == 3: # red
            print(f"\033[91m[DEBUG]: {message}\033[0m")
        elif urgency == 2: # yellow
            print(f"\033[93m[DEBUG]: {message}\033[0m")
        elif urgency == 1: # green
            print(f"\033[92m[DEBUG]: {message}\033[0m")
        # print(f"\033[91m[DEBUG]: {message}\033[0m")

def get_debug_mode():
    try:
        with open("config/debug_mode.txt", "r") as f:
            debug_mode = f.read().strip().lower()
            if debug_mode == "true":
                log("Debug mode is enabled", "Info", "Debug mode is set to True.")
                dprint("Debug mode is enabled, debug messages will be printed.", 1)
                input("Debug mode is enabled. Press Enter to continue...")
                return True
            elif debug_mode == "false":
                log("Debug mode is disabled", "Info", "Debug mode is set to False.")
                dprint("Debug mode is disabled, no debug messages will be printed.", 1)
                input("Debug mode is disabled. Press Enter to continue...")
                return False
            else:
                log("Invalid debug mode value", "Error", "Debug mode should be 'true' or 'false'.")
                dprint("Invalid debug mode value, defaulting to False.", 1)
                input("Invalid debug mode value. Press Enter to continue...")
                return False
    except FileNotFoundError:
        log("Debug mode file not found", "Warning", "Defaulting to debug mode as False.")
        dprint("Debug mode file not found, defaulting to False.", 1)
        return False
    
DEBUG_ON = get_debug_mode()

def retry(func, retries=3):
    for attempt in range(retries):
        try:
            dprint(f"Attempt {attempt + 1} for function {func.__name__}", 2)
            result = func()
            if result is False:
                log("Function returned False", "Error", f"Attempt {attempt + 1} returned False.")
                dprint(f"Attempt {attempt + 1} for function {func.__name__} returned False.", 3)
                if attempt == retries - 1:
                    log("Max retries reached", "Error", "Failed to complete the operation after multiple attempts.")
                    dprint(f"Max retries reached for function {func.__name__} after returning False.", 3)
                    return False
                continue
            return result
        except Exception as e:
            log("Retrying due to error", "Error", f"Attempt {attempt + 1} failed with error: {e}")
            dprint(f"Attempt {attempt + 1} failed for function {func.__name__} with error: {e}", 2)
            if attempt == retries - 1:
                log("Max retries reached", "Error", "Failed to complete the operation after multiple attempts.")
                dprint(f"Max retries reached for function {func.__name__} with error: {e}", 3)
                return False