import pytest
from click.testing import CliRunner

from lambda_packager.cli import cli


def test_package_function(runner: CliRunner) -> None:
    source_directory = "../data/lambda1"

    result = runner.invoke(
        cli,
        [
            "package-function",
            "--function-name",
            "test-function",
            "--source-dir",
            source_directory,
            "--output-dir",
            "dist",
        ],
    )
    assert result.exit_code == 0
    assert "Packaging Lambda function: test-function" in result.output
    assert f"Source directory: {source_directory}" in result.output
    assert "Output directory: dist" in result.output


def test_package_layer(runner: CliRunner) -> None:
    source_directory = "../data/lambda1"

    result = runner.invoke(
        cli,
        [
            "package-layer",
            "--layer-name",
            "test-layer",
            "--source-dir",
            source_directory,
            "--output-dir",
            "dist",
        ],
    )
    assert result.exit_code == 0
    assert "Packaging Lambda layer: test-layer" in result.output
    assert f"Source directory: {source_directory}" in result.output
    assert "Output directory: dist" in result.output
