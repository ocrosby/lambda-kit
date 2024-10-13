"""
This module contains tests for the directory utility functions.
"""

import os
from typing import Any, Optional

import pytest
from pytest_mock import MockerFixture

from lambda_kit.utils.directory import create_directory, validate_directory


@pytest.mark.parametrize(
    "directory, expected_exception, expected_message",
    [
        (os.getcwd(), None, None),  # Valid directory
        ("", ValueError, "Directory cannot be empty."),  # Empty directory string
        (
            "non_existent_directory",
            NotADirectoryError,
            "non_existent_directory is not a valid directory.",
        ),  # Non-existent directory
    ],
    ids=["valid_directory", "empty_directory", "non_existent_directory"],
)
def test_validate_directory(
    directory: str, expected_exception: Optional[Any], expected_message: str
) -> None:
    if expected_exception:
        with pytest.raises(expected_exception, match=expected_message):
            validate_directory(directory)
    else:
        try:
            validate_directory(directory)
        except (ValueError, NotADirectoryError) as e:
            pytest.fail(f"validate_directory raised an exception: {e}")


def test_create_directory(mocker: MockerFixture) -> None:
    """
    Test the create_directory function.

    :param mocker: The pytest mocker fixture.
    """
    # Arrange
    directory = "test_directory"
    logger = mocker.Mock()

    # Mock os.makedirs
    mock_makedirs = mocker.patch("os.makedirs")

    # Act
    create_directory(directory, logger)

    # Assert
    mock_makedirs.assert_called_once_with(directory, exist_ok=True)
    logger.info.assert_called_once_with(f"Created directory: {directory}")
