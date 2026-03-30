import random
from core.failure_injection import should_fail

def process_payment():
    if should_fail():
        return False
    return random.choice([True, True, False])  # mostly success