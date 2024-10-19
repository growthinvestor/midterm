import logging

logger = logging.getLogger(__name__)

def add(a, b):
    try:
        result = a + b
        logger.info(f"Add: {a} + {b} = {result}")
        return result
    except TypeError as e:
        logger.error(f"Error adding {a} and {b}: {e}")
        raise

def subtract(a, b):
    try:
        result = a - b
        logger.info(f"Subtract: {a} - {b} = {result}")
        return result
    except TypeError as e:
        logger.error(f"Error subtracting {a} and {b}: {e}")
        raise

# Add multiply and divide functions similarly
