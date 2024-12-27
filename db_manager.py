import config
import json
import os
import logging

# Імпорт логера з logger_config
from logger_config import logger

def get_tasks(pathname: str = config.JSON_FILE):
    try:
        # Check if file exists
        if not os.path.exists(pathname):
            logger.critical(f"File {pathname} does not exist. Exiting the program.")
            exit(1)

        # Attempt to read the file
        with open(pathname, "r") as file:
            data = json.load(file)
            return data

    except json.JSONDecodeError:
        # Error if file is empty or not valid JSON
        logger.error(f"File {pathname} is empty or contains invalid JSON. Returning an empty list.")
        return []

    except PermissionError:
        # Error accessing the file
        logger.critical(f"Insufficient permissions to access the file {pathname}.")
        return []

    except Exception as e:
        # Other unforeseen errors
        logger.exception(f"An error occurred while reading the file {pathname}: {e}")
        return []


def save_tasks(data, pathname: str = config.JSON_FILE):
    try:
        # Attempt to write data to the file
        with open(pathname, "w") as file:
            json.dump(data, file, indent=4)

    except PermissionError:
        # Error accessing the file for writing
        logger.critical(f"Insufficient permissions to write to the file {pathname}.")
        exit(1)

    except Exception as e:
        # Other unforeseen errors
        logger.exception(f"An error occurred while saving to the file {pathname}: {e}")
        exit(1) 

