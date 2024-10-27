"""
This module contains the FunctionController class.
"""

import os
import sys
from typing import Any

from jinja2 import Environment, FileSystemLoader

from lambda_kit.mvc.models import FunctionModel
from lambda_kit.mvc.views import FunctionView
from lambda_kit.utils.aws_lambda import is_python_lambda


class FunctionController:
    """
    The FunctionController class is responsible for managing Lambda functions.
    """

    def __init__(self, model: FunctionModel, view: FunctionView):
        """
        Initialize a new FunctionController
        """
        self.model = model
        self.view = view

    def initialize(self) -> None:
        """
        Initialize a new Lambda function.
        """
        lambda_template_name = "lambda_function_template.jinja2"

        if self.model.source_dir is None:
            raise ValueError("Source directory not set.")

        if os.path.isdir(self.model.source_dir):
            raise FileExistsError(
                f"The directory '{self.model.source_dir}' already exists."
            )

        # Set up the Jinja2 environment
        template_dir = "templates"
        env = Environment(loader=FileSystemLoader(template_dir))

        # Load the template
        template = env.get_template(lambda_template_name)

        context: dict[str, Any] = {
            "description": "A new Lambda function",
            "status_code": 200,
            "body_message": "Hello, World!",
        }

        # Render the template with the provided context
        rendered_content = template.render(context)

        # Write the rendered content to the output file
        self.view.info("Initializing a new Lambda function.")
        os.makedirs(self.model.source_dir)

        output_path = os.path.join(self.model.source_dir, "handler.py")
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(rendered_content)

        # Add your initialization logic here
        self.view.info(f"Lambda function initialized in {self.model.source_dir}.")

    def describe(self) -> None:
        """
        Describe the contents of a Lambda function.
        """

    def package(self) -> None:
        """
        Package a Lambda function.
        """
        self.view.info(f"Packaging Lambda function: {self.model.name}")
        self.view.info(f"Source directory: {self.model.source_dir}")
        self.view.info(f"Output directory: {self.model.output_dir}")
        # Add your packaging logic here

        if self.model.source_dir is None:
            raise ValueError("Source directory not set.")

        if is_python_lambda(self.model.source_dir, self.view.info):
            self.view.info(f"Todo: Package Lambda function: {self.model.name}")
        else:
            self.view.info(f"{self.model.source_dir} isn't a Python Lambda function.")
            sys.exit(1)

    @staticmethod
    def create() -> "FunctionController":
        """
        Create a new FunctionController.
        """
        function_model = FunctionModel()
        function_view = FunctionView()
        function_controller = FunctionController(
            model=function_model, view=function_view
        )

        return function_controller


# def create_function_mvc(
#     source_dir: str, output_dir: str, info: Callable[[str], None]
# ) -> FunctionController:
#     """
#     Create a model, view, and controller for a Lambda layer.
#
#     :param source_dir: The path to the source directory.
#     :param output_dir: The path to the output directory.
#     :param info: The info function for displaying messages.
#     :return: A tuple containing the model, view, and controller.
#     """
#     function_model = FunctionModel(
#         name=os.path.basename(os.path.normpath(source_dir)),
#         source_dir=source_dir,
#         output_dir=output_dir,
#     )
#     function_view = FunctionView(info=info)
#     function_controller = FunctionController(model=function_model, view=function_view)
#
#     return function_controller
