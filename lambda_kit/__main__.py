"""
This module contains the CLI tool for packaging Python Lambda functions.
"""

import os
import sys

import click

from jinja2 import Environment, FileSystemLoader

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
@click.option(
    "--source-dir",
    required=True,
    type=click.Path(exists=True),
    help="Path to the source directory.",
)
def initialize_function(source_dir: str) -> None:
    """Initialize a new Lambda function."""
    LAMBDA_TEMPLATE_NAME = "lambda_function_template.jinja2"

    if os.path.isdir(source_dir):
        logger.error(f"The directory '{source_dir}' already exists.")
        sys.exit(1)

    # Set up the Jinja2 environment
    template_dir = "templates"
    env = Environment(loader=FileSystemLoader(template_dir))

    # Load the template
    template = env.get_template(LAMBDA_TEMPLATE_NAME)

    context = {}

    # Render the template with the provided context
    rendered_content = template.render(context)

    # Write the rendered content to the output file
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(rendered_content)

    click.echo("Initializing a new Lambda function.")
    os.mkdirs(source_dir, exists_ok=True)
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
