"""
This module contains tests for the file utility functions.
"""

from pytest_mock import MockerFixture

from lambda_kit.utils.file import create_file


def test_create_file(mocker: MockerFixture) -> None:
    """
    Test the create_file function.

    :param mocker: The pytest mocker fixture.
    """
    # Arrange
    file_path = "test.txt"
    content = "Hello, World!"
    logger = mocker.Mock()

    mock_open_func = mocker.patch("builtins.open", mocker.mock_open())

    # Act
    create_file(file_path, content, logger)

    # Assert
    mock_open_func.assert_called_once_with(file_path, "w", encoding="utf8")
    mock_open_func().write.assert_called_once_with(content)

    logger.info.assert_called_once_with(f"Created file: {file_path}")
