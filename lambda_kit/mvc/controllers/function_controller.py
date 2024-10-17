"""
This module contains the FunctionController class.
"""

import os
from typing import Any

from jinja2 import Environment, FileSystemLoader

from lambda_kit.mvc.models import FunctionModel
from lambda_kit.mvc.views import FunctionView


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

    def initialize(self, source_dir: str) -> None:
        """
        Initialize a new Lambda function.
        """
        lambda_template_name = "lambda_function_template.jinja2"

        if os.path.isdir(source_dir):
            raise FileExistsError(f"The directory '{source_dir}' already exists.")

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
        os.makedirs(source_dir)

        output_path = os.path.join(source_dir, "handler.py")
        with open(output_path, "w", encoding="utf-8") as output_file:
            output_file.write(rendered_content)

        # Add your initialization logic here
        self.view.info(f"Lambda function initialized in {source_dir}.")

    def describe(self) -> None:
        """
        Describe the contents of a Lambda function.
        """

    def package(self) -> None:
        """
        Package a Lambda function.
        """
