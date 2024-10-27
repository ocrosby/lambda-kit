from click.testing import CliRunner

from lambda_kit.__main__ import cli


def test_describe_function():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(cli, args=["function", "describe"])

    # Assert
    assert result.exit_code == 0
    assert result.output == "Describing a Lambda function.\n"


def test_describe_layer():
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(cli, args=["layer", "describe"])

    # Assert
    assert result.exit_code == 0
    assert result.output == "Describing a Lambda layer.\n"


def test_package_layer(mocker):
    # Arrange
    runner = CliRunner()

    mock_is_python_layer = mocker.patch(
        "lambda_kit.utils.aws_lambda.is_python_layer", return_value=True
    )
    mock_logger = mocker.patch("lambda_kit.utils.logger.logger")
    source_dir = "test_source_dir"
    output_dir = "test_output_dir"
    layer_name = "test_layer"

    # Act
    result = runner.invoke(
        cli,
        [
            "layer",
            "pack",
            "--name",
            layer_name,
            "--source-dir",
            source_dir,
            "--output-dir",
            output_dir,
        ],
    )

    # Assert
    assert result.exit_code == 0
    assert f"Packaging Lambda layer: {layer_name}" in result.output
    assert f"Source directory: {source_dir}" in result.output
    assert f"Output directory: {output_dir}" in result.output
    mock_is_python_layer.assert_called_once_with(source_dir, mock_logger)
