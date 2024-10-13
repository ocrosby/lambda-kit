"""
This module contains utility functions for working with directories.
"""

# directory_utils.py

import logging
import os


def validate_directory(directory: str) -> None:
    """
    Validate the directory.

    :param directory: The directory to validate.
    :raises ValueError: If the directory is empty.
    :raises NotADirectoryError: If the directory does not exist.
    """
    directory = directory.strip()
    if directory == "":
        raise ValueError("Directory cannot be empty.")

    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a valid directory.")


def create_directory(directory: str, logger: logging.Logger) -> None:
    """
    Create a directory if it does not exist.

    :param directory: The directory to create.
    :param logger: The logger to use.
    """
    os.makedirs(directory, exist_ok=True)
    logger.info(f"Created directory: {directory}")
