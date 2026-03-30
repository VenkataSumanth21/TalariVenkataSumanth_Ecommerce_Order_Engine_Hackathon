def process_events(events):
    for event in events:
        success = event()
        if not success:
            print("Event failed → stopping flow")
            return False
    return True