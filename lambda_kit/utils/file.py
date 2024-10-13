"""
This module contains utility functions for working with files.
"""

# file_utils.py

import logging


def create_file(file_path: str, content: str, logger: logging.Logger) -> None:
    """
    Create a file with the given content.

    :param file_path: The path to the file.
    :param content: The content to write to the file.
    :param logger: The logger to use.
    """
    with open(file_path, "w", encoding="utf8") as f:
        f.write(content)
    logger.info(f"Created file: {file_path}")
