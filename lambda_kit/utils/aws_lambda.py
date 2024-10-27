"""
This module contains utility functions for working with AWS Lambda functions.
"""

# function_model.py

import ast
import os
from typing import Callable, Optional

from lambda_kit.utils.directory import validate_directory


def is_dict_annotation(annotation: Optional[ast.expr]) -> bool:
    return isinstance(annotation, ast.Name) and annotation.id == "dict"


def is_context_annotation(annotation: Optional[ast.expr]) -> bool:
    return isinstance(annotation, ast.Attribute) and annotation.attr == "Context"


def has_lambda_handler_signature(node: ast.FunctionDef) -> bool:
    if len(node.args.args) != 2:
        return False
    param1, param2 = node.args.args
    return is_dict_annotation(param1.annotation) and is_context_annotation(
        param2.annotation
    )


def contains_lambda_handler_code(python_source_code: str) -> bool:
    """
    Determine if the given code contains a lambda handler function.

    Parameters:
    code (str): The Python code to check.

    Returns:
    bool: True if the code contains a lambda handler function, False otherwise.
    """
    try:
        tree = ast.parse(python_source_code)
        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue

            if not has_lambda_handler_signature(node):
                continue

            return True
        return False
    except SyntaxError:
        return False


def is_python_lambda(directory: str, info: Callable[[str], None]) -> bool:
    """
    Determine if a given directory appears to be a Python Lambda function.

    :param directory: The directory to check.
    :return: True if it is a Python Lambda function, False otherwise.
    :raises ValueError: If the directory is empty.
    :raises NotADirectoryError: If the directory does not exist.
    """
    validate_directory(directory)

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".py"):
            info(f"Checking file: {file_path}")
            with open(file_path, "r", encoding="utf-8") as file:
                code = file.read()
                if contains_lambda_handler_code(code):
                    info(f"Found lambda handler in file: {file_path}")
                    return True

    info(f"No lambda handler found in any Python file at the root of {directory}.")
    return False


def is_python_layer(directory: str, info: Callable[[str], None]) -> bool:
    """
    Determine if a given directory appears to be a Python Lambda layer.

    :param directory: The directory to check.
    :param info: The callable function to use for output.
    :return: True if it is a Python Lambda layer, False otherwise.
    :raises ValueError: If the directory is empty.
    :raises NotADirectoryError: If the directory does not exist.
    """
    validate_directory(directory)

    required_files = ["python", "requirements.txt"]

    for file in required_files:
        file_path = os.path.join(directory, file)
        if os.path.isdir(file_path):
            info(f"Found required directory: {file_path}")
        else:
            info(f"Missing required directory: {file_path}")
            return False

    info(f"{directory} appears to be a Python Lambda layer.")

    return True
