from lambda_kit.utils.aws_lambda import contains_lambda_handler_code


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
