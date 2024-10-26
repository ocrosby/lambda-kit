"""
This module contains the CLI tool for packaging Python Lambda functions.
"""

import os
import sys
from curses.ascii import controlnames

import click

from lambda_kit.mvc.controllers.layer_controller import LayerController, create_layer_mvc
from lambda_kit.mvc.controllers.function_controller import FunctionController, create_function_mvc
from lambda_kit.mvc.models import FunctionModel, LayerModel
from lambda_kit.mvc.views import FunctionView, LayerView
from lambda_kit.utils.aws_lambda import is_python_lambda, is_python_layer
from lambda_kit.utils.logger import logger


@click.group()
def cli() -> None:
    """CLI tool for manipulating Python Lambda components."""


@cli.group()
def function() -> None:
    """Commands for manipulating Lambda functions."""


@cli.group()
def layer() -> None:
    """Commands for manipulating Lambda layers."""


@function.command("init")
@click.argument("source-dir")
def initialize_function(source_dir: str) -> None:
    """
    Initialize a new Lambda function.

    :param source_dir: The path to the source directory.
    :return: None
    """
    try:
        model, view, controller = create_function_mvc(source_dir, click.echo)
        controller.initialize(source_dir)
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@function.command("describe")
def describe_function() -> None:
    """Describe a Lambda function."""
    click.echo("Describing a Lambda function.")
    # Add your description logic here


@function.command("pack")
@click.option("-n", "--name", required=True, help="Name of the Lambda function.")
@click.option(
    "--source-dir",
    required=True,
    type=click.Path(exists=True),
    help="Path to the source directory.",
)
@click.option(
    "--output-dir",
    required=True,
    type=click.Path(),
    help="Path to the output directory.",
)
def package_function(function_name: str, source_dir: str, output_dir: str) -> None:
    """Package Lambda functions."""
    click.echo(f"Packaging Lambda function: {function_name}")
    click.echo(f"Source directory: {source_dir}")
    click.echo(f"Output directory: {output_dir}")
    # Add your packaging logic here

    if is_python_lambda(source_dir, logger):
        click.echo(f"Todo: Package Lambda function: {function_name}")
    else:
        click.echo(f"{source_dir} does not appear to be a Python Lambda function.")
        sys.exit(1)


@layer.command("init")
@click.argument("source-dir")
def initialize_layer(source_dir: str) -> None:
    """Initialize a new Lambda layer."""
    model: LayerModel
    view: LayerView
    controller: LayerController

    try:
        model, view, controller = create_layer_mvc(source_dir, click.echo)
        controller.initialize()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@layer.command("describe")
@click.argument("source-dir")
def describe_layer(source_dir: str) -> None:
    """Describe a Lambda layer."""
    model: LayerModel
    view: LayerView
    controller: LayerController

    try:
        model, view, controller = create_layer_mvc(source_dir, click.echo)
        controller.describe()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@layer.command("pack")
@click.option("-n", "--name", required=True, help="Name of the Lambda layer.")
@click.option(
    "--source-dir",
    required=True,
    type=click.Path(exists=True),
    help="Path to the source directory.",
)
@click.option(
    "--output-dir",
    required=True,
    type=click.Path(),
    help="Path to the output directory.",
)
def package_layer(layer_name: str, source_dir: str, output_dir: str) -> None:
    """Package Lambda layers."""
    model: LayerModel
    view: LayerView
    controller: LayerController

    try:
        model, view, controller = create_layer_mvc(source_dir, click.echo)
        controller.package()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


def main() -> None:
    """
    Entry point for the CLI tool.

    :return:
    """
    cli()


if __name__ == "__main__":
    main()
