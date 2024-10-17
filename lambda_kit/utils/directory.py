"""
This module contains utility functions for working with directories.
"""

# directory_utils.py

import logging
import os


def touch_directory(directory: str, logger: logging.Logger) -> None:
    """
    Create an empty directory.

    :param directory: The path to the directory.
    :param logger: The logger to use.
    """
    os.makedirs(directory, exist_ok=True)
    logger.info(f"Created directory: {directory}")


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


def create_virtual_environment(directory: str, logger: logging.Logger) -> None:
    """
    Create a virtual environment in the given directory.

    :param directory: The directory to create the virtual environment in.
    :param logger: The logger to use.
    """
    venv_dir = os.path.join(directory, "python")

    if os.path.isdir(venv_dir):
        logger.error("The directory '%s' already exists.", venv_dir)
        return

    os.makedirs(venv_dir)
    logger.info(f"Created virtual environment: {venv_dir}")
