"""
This module contains the CLI tool for packaging Python Lambda functions.
"""

import os
import sys

import click

from lambda_kit.mvc.controllers.function_controller import FunctionController
from lambda_kit.mvc.controllers.layer_controller import LayerController


@click.group()
def cli() -> None:
    """CLI tool for manipulating Python Lambda components."""


@cli.group()
def function() -> None:
    """Commands for manipulating Lambda functions."""


@cli.group()
def layer() -> None:
    """Commands for manipulating Lambda layers."""


def echo_wrapper(message: str) -> None:
    """Wrapper for click.echo."""
    click.echo(message)

@function.command("init")
@click.argument("source-dir")
@click.option(
    "--output-dir",
    required=True,
    type=click.Path(),
    help="Path to the output directory.",
)
def initialize_function(source_dir: str, output_dir: str) -> None:
    """Initialize a new Lambda function."""
    try:
        controller = FunctionController.create()
        model = controller.model
        view = controller.view

        view.info_display_func = echo_wrapper
        view.error_display_func = echo_wrapper

        model.name = os.path.basename(os.path.normpath(source_dir))
        model.source_dir = source_dir
        model.output_dir = output_dir

        controller.initialize()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@function.command("describe")
@click.argument("source-dir")
@click.option(
    "--output-dir",
    required=True,
    type=click.Path(),
    help="Path to the output directory.",
)
def describe_function(source_dir: str, output_dir: str) -> None:
    """Describe a Lambda function."""
    try:
        controller = FunctionController.create()
        model = controller.model
        view = controller.view

        view.info_display_func = echo_wrapper
        view.error_display_func = echo_wrapper

        model.source_dir = source_dir
        model.output_dir = output_dir

        controller.describe()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@function.command("pack")
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
def package_function(source_dir: str, output_dir: str) -> None:
    """Package Lambda functions."""
    try:
        controller = FunctionController.create()
        model = controller.model
        view = controller.view

        view.info_display_func = echo_wrapper
        view.error_display_func = echo_wrapper

        model.source_dir = source_dir
        model.output_dir = output_dir

        controller.package()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@layer.command("init")
@click.argument("source-dir")
@click.option(
    "--output-dir",
    required=True,
    type=click.Path(),
    help="Path to the output directory.",
)
def initialize_layer(source_dir: str, output_dir: str) -> None:
    """Initialize a new Lambda layer."""
    try:
        controller = LayerController.create()
        model = controller.model
        view = controller.view

        view.info_display_func = echo_wrapper
        view.error_display_func = echo_wrapper

        model.name = os.path.basename(os.path.normpath(source_dir))
        model.source_dir = source_dir
        model.output_dir = output_dir

        controller.initialize()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@layer.command("describe")
@click.argument("source-dir")
@click.option(
    "--output-dir",
    required=True,
    type=click.Path(),
    help="Path to the output directory.",
)
def describe_layer(source_dir: str, output_dir: str) -> None:
    """Describe a Lambda layer."""
    try:
        controller = LayerController.create()
        model = controller.model
        view = controller.view

        view.info_display_func = echo_wrapper
        view.error_display_func = echo_wrapper

        model.source_dir = source_dir
        model.output_dir = output_dir

        controller.describe()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)


@layer.command("pack")
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
def package_layer(source_dir: str, output_dir: str) -> None:
    """Package Lambda layers."""
    try:
        controller = LayerController.create()
        model = controller.model
        view = controller.view

        view.info_display_func = echo_wrapper
        view.error_display_func = echo_wrapper

        model.source_dir = source_dir
        model.output_dir = output_dir

        controller.package()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)
