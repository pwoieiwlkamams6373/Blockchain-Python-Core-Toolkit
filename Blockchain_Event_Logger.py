import logging
logging.basicConfig(filename="events.log", level=logging.INFO)

class EventLogger:
    def log_event(self, event_type, data):
        logging.info(f"{event_type}: {data}")

if __name__ == "__main__":
    logger = EventLogger()
    logger.log_event("BLOCK_MINED", {"height":10})
    print("事件已记录")
