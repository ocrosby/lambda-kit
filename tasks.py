from invoke import Context, task  # type: ignore[attr-defined]


@task(aliases=["c"])
def clean(c: Context) -> None:
    """Clean up build artifacts."""
    c.run("find . -name '*.pyc' -delete")
    c.run("find . -name '.coverage' -delete")
    c.run("find . -name 'junit.xml' -delete")

    c.run("find . -name '*.egg-info' -type d -exec rm -r {} +")
    c.run("find . -name '.mypy_cache' -type d -exec rm -r {} +")
    c.run("find . -name '.pytest_cache' -type d -exec rm -r {} +")
    c.run("find . -name '__pycache__' -type d -exec rm -r {} +")
    c.run("find . -name 'dist' -type d -exec rm -r {} +")
    c.run("find . -name 'build' -type d -exec rm -r {} +")


@task(aliases=["i"], help={"dev": "Install development dependencies."})
def install(c: Context, dev: bool = False) -> None:
    """Install dependencies."""
    if dev:
        c.run("echo 'Installing development dependencies ...'")
        c.run("pip install -e .[dev]")
    else:
        c.run("echo 'Installing dependencies ...'")
        c.run("pip install .")


@task(aliases=["l"])
def lint(c: Context) -> None:
    """Run linters (flake8 and pylint)."""
    c.run("echo 'Running linters ...'")
    c.run("flake8 lambda_packager tests setup.py tasks.py")
    c.run("pylint lambda_packager tests setup.py tasks.py")
    c.run("mypy lambda_packager tests setup.py tasks.py")


@task(aliases=["t"])
def test(c: Context) -> None:
    """Run tests."""
    c.run("echo 'Running tests ...'")
    c.run("pytest")


@task(aliases=["f"])
def format_code(c: Context) -> None:
    """Format code with black and isort."""
    c.run("echo 'Formatting code ...'")
    c.run("black .")
    c.run("isort .")


@task(aliases=["p"])
def package(c: Context) -> None:
    """Package the CLI tool."""
    c.run("echo 'Packaging the project ...'")
    c.run("python setup.py sdist bdist_wheel")


@task(pre=[clean])
def run_all_tasks(c: Context) -> None:
    """Run all tasks."""
    clean(c)
    lint(c)
    test(c)
