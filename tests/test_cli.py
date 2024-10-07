import pytest
from click.testing import CliRunner

from lambda_packager.cli import cli


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_package_function(runner, monkeypatch):
    # Mock os.path.exists to always return True
    monkeypatch.setattr("os.path.exists", lambda x: True)

    result = runner.invoke(
        cli,
        [
            "package-function",
            "--function-name",
            "test-function",
            "--source-dir",
            "src",
            "--output-dir",
            "dist",
        ],
    )
    assert result.exit_code == 0
    assert "Packaging Lambda function: test-function" in result.output
    assert "Source directory: src" in result.output
    assert "Output directory: dist" in result.output


def test_package_layer(runner):
    result = runner.invoke(
        cli,
        [
            "package-layer",
            "--layer-name",
            "test-layer",
            "--source-dir",
            "src",
            "--output-dir",
            "dist",
        ],
    )
    assert result.exit_code == 0
    assert "Packaging Lambda layer: test-layer" in result.output
    assert "Source directory: src" in result.output
    assert "Output directory: dist" in result.output
