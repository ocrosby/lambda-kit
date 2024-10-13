"""
This module contains the CLI tool for packaging Python Lambda functions.
"""

import sys

import click

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
def initialize_function() -> None:
    """Initialize a new Lambda function."""
    click.echo("Initializing a new Lambda function.")
    # Add your initialization logic here


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
def initialize_layer() -> None:
    """Initialize a new Lambda layer."""
    click.echo("Initializing a new Lambda layer.")
    # Add your initialization logic here


@layer.command("describe")
def describe_layer() -> None:
    """Describe a Lambda layer."""
    click.echo("Describing a Lambda layer.")
    # Add your description logic here


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
    click.echo(f"Packaging Lambda layer: {layer_name}")
    click.echo(f"Source directory: {source_dir}")
    click.echo(f"Output directory: {output_dir}")
    # Add your packaging logic here

    if is_python_layer(source_dir, logger):
        click.echo(f"Todo: Package Lambda layer: {layer_name}")
    else:
        click.echo(f"{source_dir} does not appear to be a Python Lambda layer.")
        sys.exit(1)


def main() -> None:
    """
    Entry point for the CLI tool.

    :return:
    """
    cli()


if __name__ == "__main__":
    main()
