import logging
import os

def get_logger(name: str):
    level = os.getenv("LOG_LEVEL", "INFO")
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if logger already exists
    if not logger.handlers:
        # CONSOLE HANDLER
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(message)s", datefmt="%H:%M:%S")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # FILE HANDLER
        file_handler = logging.FileHandler("migration.log")
        file_formatter = logging.Formatter("%(asctime)s | %(levelname)-7s | %(name)-15s | %(message)s")
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    logger.propagate = False
    return logger
