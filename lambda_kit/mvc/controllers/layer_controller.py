"""
This module contains the LayerController class.
"""

import os
import sys
from typing import Callable

from lambda_kit.mvc.models import LayerModel
from lambda_kit.mvc.views import LayerView
from lambda_kit.utils.aws_lambda import is_python_lambda, is_python_layer


class LayerController:
    """
    The LayerController class is responsible for managing Lambda layers.
    """

    def __init__(self, model: LayerModel, view: LayerView):
        """
        Initialize a new LayerController with a view and a model.
        """
        self.model = model
        self.view = view

    def initialize(self) -> None:
        """
        Initialize a new Lambda layer.
        """

    def describe(self) -> None:
        """
        Describe the contents of a Lambda layer.
        """

    def is_layer(self) -> bool:
        """
        Determine if the current directory is a Lambda layer.
        """
        validate_directory(self.model.source_dir)

        required_files = ["python", "requirements.txt"]

        for file in required_files:
            file_path = os.path.join(self.model.source_dir, file)
            if os.path.isdir(file_path):
                self.view.info(f"Found required directory: {file_path}")
            else:
                self.view.info(f"Missing required directory: {file_path}")
                return False

        self.view.info(f"{directory} appears to be a Python Lambda layer.")

        return True

    def package(self) -> None:
        """
        Package a Lambda layer.
        """
        self.view.info(f"Packaging Lambda layer: {self.model.name}")
        self.view.info(f"Source directory: {self.model.source_dir}")
        self.view.info(f"Output directory: {self.model.output_dir}")
        # Add your packaging logic here

        if is_python_layer(self.model.source_dir, self.view.info):
            self.view.info(f"Todo: Package Lambda layer: {self.model.name}")
        else:
            self.view.info(
                f"{self.model.source_dir} does not appear to be a Python Lambda layer."
            )
            sys.exit(1)


def create_layer_mvc(
    source_dir: str, info: Callable
) -> tuple[LayerModel, LayerView, LayerController]:
    """
    Create a model, view, and controller for a Lambda layer.

    :param source_dir: The path to the source directory.
    :param info: The info function for displaying messages.
    :return: A tuple containing the model, view, and controller.
    """
    layer_model = LayerModel(
        layer_name=os.path.basename(os.path.normpath(source_dir)),
        source_dir=source_dir,
    )
    layer_view = LayerView(info=info)
    layer_controller = LayerController(model=layer_model, view=layer_view)

    return layer_model, layer_view, layer_controller
