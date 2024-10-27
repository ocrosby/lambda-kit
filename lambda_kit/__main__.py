"""
This module contains the CLI tool for packaging Python Lambda functions.
"""

import sys

import click

from lambda_kit.mvc.controllers.function_controller import create_function_mvc
from lambda_kit.mvc.controllers.layer_controller import create_layer_mvc


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
@click.option(
    "--output-dir",
    required=True,
    type=click.Path(),
    help="Path to the output directory.",
)
def initialize_function(source_dir: str, output_dir: str) -> None:
    """Initialize a new Lambda function."""
    try:
        create_function_mvc(source_dir, output_dir, click.echo).initialize()
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
        create_function_mvc(source_dir, output_dir, click.echo).describe()
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
        create_function_mvc(source_dir, output_dir, click.echo).package()
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
        create_layer_mvc(source_dir, output_dir, click.echo).initialize()
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
        create_layer_mvc(source_dir, output_dir, click.echo).describe()
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
        create_layer_mvc(source_dir, output_dir, click.echo).package()
    except FileExistsError as err:
        click.echo(err)
        sys.exit(1)
