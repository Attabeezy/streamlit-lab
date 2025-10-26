import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_event(event):
    """Log events for tracking and debugging."""
    logging.info(event)
