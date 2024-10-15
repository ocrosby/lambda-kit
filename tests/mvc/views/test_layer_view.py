# tests/mvc/views/test_layer_view.py
from pytest_mock import MockerFixture

from lambda_kit.mvc.views.layer_view import LayerView
from tests.mvc.views.helpers import view_error_test, view_info_test


def test_layer_view_info(mocker: MockerFixture) -> None:
    view_info_test(LayerView, mocker)


def test_layer_view_error(mocker: MockerFixture) -> None:
    view_error_test(LayerView, mocker)
