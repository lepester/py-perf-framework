# utils/logger.py

import logging


def setup_logger():
    """
    Sets up a logger for the performance testing framework.

    Configures the logging system to log messages at the INFO level
    and higher. The log messages will include the timestamp, the
    severity level of the message, and the message itself.

    :return: A logger instance configured for performance testing.
    """
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level to INFO
        format="%(asctime)s - %(levelname)s - %(message)s"  # Log message format
    )
    return logging.getLogger("performance_test")  # Create and return a logger instance
