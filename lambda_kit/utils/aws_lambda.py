"""
This module contains utility functions for working with AWS Lambda functions.
"""

# aws_lambda.py

import logging
import os
from typing import Callable

from lambda_kit.utils.directory import create_directory, validate_directory
from lambda_kit.utils.file import create_file


def is_python_lambda(directory: str) -> bool:
    """
    Determine if a given directory appears to be a Python Lambda function.

    :param directory: The directory to check.
    :return: True if it is a Python Lambda function, False otherwise.
    :raises ValueError: If the directory is empty.
    :raises NotADirectoryError: If the directory does not exist.
    """
    validate_directory(directory)

    required_files = ["lambda_function.py", "requirements.txt"]

    for file in required_files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            print(f"Found required file: {file_path}")
        else:
            print(f"Missing required file: {file_path}")
            return False

    print(f"{directory} appears to be a Python Lambda function.")
    return True


def is_python_layer(directory: str) -> bool:
    """
    Determine if a given directory appears to be a Python Lambda layer.

    :param directory: The directory to check.
    :return: True if it is a Python Lambda layer, False otherwise.
    :raises ValueError: If the directory is empty.
    :raises NotADirectoryError: If the directory does not exist.
    """
    validate_directory(directory)

    required_files = ["python", "requirements.txt"]

    for file in required_files:
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            print(f"Found required directory: {file_path}")
        else:
            print(f"Missing required directory: {file_path}")
            return False

    print(f"{directory} appears to be a Python Lambda layer.")
    return True


def create_local_lambda_function(
    directory: str,
    function_name: str,
    logger: logging.Logger,
    create_file_func: Callable[[str, str, logging.Logger], None] = create_file,
    create_dir_func: Callable[[str, logging.Logger], None] = create_directory,
) -> None:
    """
    Create a new AWS Lambda function locally.

    :param directory: The directory where the Lambda function will be created.
    :param function_name: The name of the Lambda function.
    :param logger: The logger to use.
    :param create_file_func: The function to create a file.
    :param create_dir_func: The function to create a directory.
    :raises ValueError: If the directory is empty.
    :raises NotADirectoryError: If the directory does not exist.
    """
    # Validate the directory
    validate_directory(directory)

    create_dir_func(directory, logger)

    # Create the Lambda function directory
    function_dir = os.path.join(directory, function_name)
    create_dir_func(function_dir, logger)

    # Create a sample lambda_function.py file
    lambda_function_content = """def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
"""
    create_file_func(
        os.path.join(function_dir, "lambda_function.py"),
        lambda_function_content,
        logger,
    )

    # Create a sample requirements.txt file
    requirements_content = """# Add your dependencies here
"""
    create_file_func(
        os.path.join(function_dir, "requirements.txt"), requirements_content, logger
    )

    print(
        f"Lambda function '{function_name}' created successfully in '{function_dir}'."
    )
