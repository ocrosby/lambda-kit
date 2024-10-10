"""
This module contains the CLI tool for packaging Python Lambda layers.
"""

import click

@click.group()
def cli() -> None:
    """CLI tool for packaging Python Lambda layers."""

@cli.command("pack")
@click.option("--layer-name", required=True, help="Name of the Lambda layer.")
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

if __name__ == "__main__":
    cli()
