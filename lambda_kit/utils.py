# lambda_kit/utils.py

import logging
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


def create_file(file_path: str, content: str, logger: logging.Logger) -> None:
    """
    Create a file with the given content.

    :param file_path: The path to the file.
    :param content: The content to write to the file.
    """
    with open(file_path, "w", encoding="utf8") as f:
        f.write(content)
    logger.info(f"Created file: {file_path}")


def create_directory(directory: str, logger: logging.Logger) -> None:
    """
    Create a directory if it does not exist.

    :param directory: The directory to create.
    :param logger: The logger to use.
    """
    os.makedirs(directory, exist_ok=True)
    logger.info(f"Created directory: {directory}")


def create_local_lambda_function(
    directory: str,
    function_name: str,
    logger: logging.Logger,
    create_file_func=create_file,
    create_dir_func=create_directory,
) -> str:
    """
    Create a new AWS Lambda function locally.

    :param directory: The directory where the Lambda function will be created.
    :param function_name: The name of the Lambda function.
    :param logger: The logger to use.
    :param create_file_func: The function to create a file.
    :param create_dir_func: The function to create a directory
    :return: The path to the Lambda function directory.
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


# Example usage
# create_local_lambda_function('/path/to/your/lambda/functions', 'my_lambda_function')
