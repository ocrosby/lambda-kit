# tests/mvc/views/helpers.py
from typing import Any, Type

from pytest_mock import MockerFixture


def view_info_test(view_class: Type[Any], mocker: MockerFixture) -> None:
    # Create mock functions
    mock_info = mocker.Mock()
    mock_error = mocker.Mock()

    # Create an instance of the view class with the mock functions
    view = view_class(info=mock_info, error=mock_error)

    # Call the info method
    message = "Test info message"
    view.info(message)

    # Assert that the mock info function was called with the correct message
    mock_info.assert_called_once_with(message)


def view_error_test(view_class: Type[Any], mocker: MockerFixture) -> None:
    # Create mock functions
    mock_info = mocker.Mock()
    mock_error = mocker.Mock()

    # Create an instance of the view class with the mock functions
    view = view_class(info=mock_info, error=mock_error)

    # Call the error method
    message = "Test error message"
    view.error(message)

    # Assert that the mock error function was called with the correct message
    mock_error.assert_called_once_with(message)
