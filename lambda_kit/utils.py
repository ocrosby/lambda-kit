# lambda_kit/utils.py

import os


def validate_directory(directory: str) -> None:
    """
    Validate the directory.

    :param directory: The directory to validate.
    :return: The validated directory.
    :raises ValueError: If the directory is empty.
    :raises NotADirectoryError: If the directory does not exist.
    """
    directory = directory.strip()
    if directory == "":
        raise ValueError("Directory cannot be empty.")

    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a valid directory.")


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
