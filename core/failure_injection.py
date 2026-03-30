import random

FAILURE_MODE = False

def enable_failure():
    global FAILURE_MODE
    FAILURE_MODE = True

def disable_failure():
    global FAILURE_MODE
    FAILURE_MODE = False

def should_fail():
    if FAILURE_MODE:
        return random.choice([True, False])
    return False