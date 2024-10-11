from invoke import Collection, Context, task  # type: ignore[attr-defined]


@task(aliases=["c"])
def clean(c: Context) -> None:
    """Clean up build artifacts."""
    c.run("echo 'Cleaning up build artifacts ...'")
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

    c.run("npm install")


@task(aliases=["f"])
def format_code(c: Context) -> None:
    """Format code with black and isort."""
    c.run("echo 'Formatting code ...'")

    # Format code
    c.run("black . --exclude 'venv/*' --exclude '.venv/*'")

    # Sort imports
    c.run("isort .")


@task(aliases=["l"], pre=[format_code])
def lint(c: Context) -> None:
    """Run linters (flake8 and pylint)."""
    c.run("echo 'Analyzing Syntax ...'")
    c.run("flake8 lambda_packager tests setup.py tasks.py")
    c.run("pylint lambda_packager tests setup.py tasks.py")
    c.run("mypy lambda_packager tests setup.py tasks.py")


@task(aliases=["t"])
def test(c: Context) -> None:
    """Run tests."""
    c.run("echo 'Running tests ...'")
    c.run("pytest")


@task(aliases=["p"])
def package(c: Context) -> None:
    """Package the CLI tool."""
    c.run("echo 'Packaging the project ...'")
    c.run("python setup.py sdist bdist_wheel")


@task()
def run_all_tasks(c: Context) -> None:
    """Run all tasks."""
    lint(c)
    test(c)


# Create a collection and set the default task
ns = Collection(clean, install, lint, test, format_code, package, run_all_tasks)
ns.configure({"run": {"echo": True}})
ns.default = "run_all_tasks"
