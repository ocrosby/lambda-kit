import ast

import pytest

from lambda_kit.utils.aws_lambda import (
    contains_lambda_handler_code,
    create_local_lambda_function,
    has_lambda_handler_signature,
    is_python_lambda,
    is_python_layer,
)


def test_contains_lambda_handler_code_empty() -> None:
    """
    Test the contains_lambda_handler_code function with undefined code.

    :param mocker: The pytest mocker fixture.
    """
    # Arrange
    python_source_code = ""

    # Act
    result = contains_lambda_handler_code(python_source_code)

    # Assert
    assert not result, "Expected the code to not contain a lambda handler function."


def test_contains_lambda_true() -> None:
    """
    Test the contains_lambda_handler_code function with a valid lambda handler.

    :param mocker: The pytest mocker fixture.
    """
    # Arrange
    python_source_code = """
import json

from aws_lambda_typing import context as lambda_context


def my_handler_function(event: dict, context: lambda_context.Context) -> dict[str, any]:
    pass
"""

    # Act
    result = contains_lambda_handler_code(python_source_code)

    # Assert
    assert result, "Expected the code to contain a lambda handler function."


@pytest.mark.parametrize(
    "code, expected",
    [
        (
            """
def lambda_handler(event: dict, context: lambda_context.Context) -> dict:
    pass
""",
            True,
        ),
        (
            """
def lambda_handler(event, context):
    pass
""",
            False,
        ),
        (
            """
def lambda_handler():
    pass
""",
            False,
        ),
        (
            """
def lambda_handler(event: dict, context: lambda_context.Context, extra_param: str):
    pass
""",
            False,
        ),
    ],
)
def test_has_lambda_handler_signature(code, expected):
    tree = ast.parse(code)
    function_node = tree.body[0]
    assert has_lambda_handler_signature(function_node) == expected


@pytest.mark.parametrize(
    "directory, files, contains_lambda, expected",
    [
        ("test_dir", ["lambda_function.py"], True, True),
        ("test_dir", ["lambda_function.py"], False, False),
        ("test_dir", ["not_a_lambda.py"], False, False),
        ("empty_dir", [], False, False),
    ],
)
def test_is_python_lambda(directory, files, contains_lambda, expected, mocker):
    mocker.patch("os.listdir", return_value=files)
    mocker.patch("os.path.isfile", return_value=True)
    mocker.patch("builtins.open", mocker.mock_open(read_data=""))
    mocker.patch(
        "lambda_kit.utils.aws_lambda.contains_lambda_handler_code",
        return_value=contains_lambda,
    )
    mocker.patch("lambda_kit.utils.aws_lambda.validate_directory")
    mock_logger = mocker.Mock()

    result = is_python_lambda(directory, mock_logger)
    assert result == expected


@pytest.mark.parametrize(
    "directory, is_python_dir, is_requirements_file, expected",
    [
        ("test_dir", True, True, False),
        ("test_dir", True, False, False),
        ("test_dir", False, True, False),
        ("test_dir", False, False, False),
    ],
)
def test_is_python_layer(
    directory, is_python_dir, is_requirements_file, expected, mocker
):
    mocker.patch(
        "os.path.isdir", side_effect=lambda x: is_python_dir if "python" in x else False
    )
    mocker.patch(
        "os.path.isfile",
        side_effect=lambda x: (
            is_requirements_file if "requirements.txt" in x else False
        ),
    )
    mocker.patch("lambda_kit.utils.aws_lambda.validate_directory")
    mock_logger = mocker.Mock()

    result = is_python_layer(directory, mock_logger)
    assert result == expected


def test_create_local_lambda_function(mocker):
    # Arrange
    directory = "test_dir"
    function_name = "test_function"
    logger = mocker.Mock()

    mock_create_file = mocker.patch("lambda_kit.utils.aws_lambda.create_file")
    mock_create_directory = mocker.patch("lambda_kit.utils.aws_lambda.create_directory")
    mock_validate_directory = mocker.patch(
        "lambda_kit.utils.aws_lambda.validate_directory"
    )

    # Act
    create_local_lambda_function(
        directory, function_name, logger, mock_create_file, mock_create_directory
    )

    # Assert
    mock_validate_directory.assert_called_once_with(directory)
    mock_create_directory.assert_any_call(directory, logger)
    mock_create_directory.assert_any_call(f"{directory}/{function_name}", logger)
    mock_create_file.assert_any_call(
        f"{directory}/{function_name}/lambda_function.py",
        """def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }
""",
        logger,
    )
    mock_create_file.assert_any_call(
        f"{directory}/{function_name}/requirements.txt",
        """# Add your dependencies here
""",
        logger,
    )
