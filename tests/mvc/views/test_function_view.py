# tests/mvc/views/test_function_view.py
from pytest_mock import MockerFixture

from lambda_kit.mvc.views.function_view import FunctionView
from tests.mvc.views.helpers import view_error_test, view_info_test


def test_function_view_info(mocker: MockerFixture) -> None:
    view_info_test(FunctionView, mocker)


def test_function_view_error(mocker: MockerFixture) -> None:
    view_error_test(FunctionView, mocker)
