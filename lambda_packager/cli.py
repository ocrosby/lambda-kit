import click


@click.group()
def cli():
    """CLI tool for packaging and deploying Python Lambda functions and Lambda layers."""


@cli.command()
@click.option("--function-name", required=True, help="Name of the Lambda function.")
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
def package_function(function_name: str, source_dir: str, output_dir: str):
    """Package Lambda functions."""
    click.echo(f"Packaging Lambda function: {function_name}")
    click.echo(f"Source directory: {source_dir}")
    click.echo(f"Output directory: {output_dir}")
    # Add your packaging logic here


@cli.command()
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
def package_layer(layer_name, source_dir, output_dir):
    """Package Lambda layers."""
    click.echo(f"Packaging Lambda layer: {layer_name}")
    click.echo(f"Source directory: {source_dir}")
    click.echo(f"Output directory: {output_dir}")
    # Add your packaging logic here


if __name__ == "__main__":
    cli()
