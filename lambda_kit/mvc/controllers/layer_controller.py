"""
This module contains the LayerController class.
"""

import os
import sys
from typing import Callable

from lambda_kit.mvc.models import LayerModel
from lambda_kit.mvc.views import LayerView
from lambda_kit.utils.aws_lambda import is_python_layer


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
        self.view.info(f"Todo: Initialize Lambda layer: {self.model.name}")

    def describe(self) -> None:
        """
        Describe the contents of a Lambda layer.
        """
        self.view.info(f"Todo: Describe Lambda layer: {self.model.name}")

    def is_layer(self) -> bool:
        """
        Determine if the current directory is a Lambda layer.
        """
        if self.model.name is None:
            self.view.info("Layer name not set.")
            return False

        if self.model.source_dir is None:
            self.view.info("Source directory not set.")
            return False

        if len(self.model.source_dir) == 0:
            self.view.info("Source directory is empty.")
            return False

        if not os.path.isdir(self.model.source_dir):
            self.view.info(f"Directory not found: {self.model.source_dir}")
            return False

        required_files = ["python", "requirements.txt"]

        for file in required_files:
            file_path = os.path.join(self.model.source_dir, file)
            if os.path.isdir(file_path):
                self.view.info(f"Found required directory: {file_path}")
            else:
                self.view.info(f"Missing required directory: {file_path}")
                return False

        self.view.info(f"{self.model.source_dir} appears to be a Python Lambda layer.")

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
    source_dir: str, output_dir: str, info: Callable[[str], None]
) -> LayerController:
    """
    Create a model, view, and controller for a Lambda layer.

    :param source_dir: The path to the source directory.
    :param output_dir: The path to the output directory.
    :param info: The info function for displaying messages.
    :return: A tuple containing the model, view, and controller.
    """
    layer_model = LayerModel(
        name=os.path.basename(os.path.normpath(source_dir)),
        source_dir=source_dir,
        output_dir=output_dir,
    )
    layer_view = LayerView(info=info)
    layer_controller = LayerController(model=layer_model, view=layer_view)

    return layer_controller
