from invoke import Collection, Context, task  # type: ignore[attr-defined]


@task(aliases=["c"])
def clean(c: Context) -> None:
    """Clean up build artifacts."""
    c.run("echo 'Cleaning up build artifacts ...'")

    # Remove build artifact files
    c.run("find lambda_kit tests -name '*.pyc' -type f -delete")
    c.run("find lambda_kit tests -name '.coverage' -type f -delete")
    c.run("find lambda_kit tests -name 'junit.xml' -type f -delete")

    # Remove build artifact directories
    c.run("find lambda_kit tests -name '*.egg-info' -type d -exec rm -r {} +")
    c.run("find lambda_kit tests -name '.mypy_cache' -type d -exec rm -r {} +")
    c.run("find lambda_kit tests -name '.pytest_cache' -type d -exec rm -r {} +")
    c.run("find lambda_kit tests -name '__pycache__' -type d -exec rm -r {} +")

    c.run("rm -f junit.xml")
    c.run("rm -f .coverage")
    c.run("rm -rf .tox/")
    c.run("rm -rf dist/")
    c.run("rm -rf build/")
    c.run("rm -rf *.egg-info")

    # Clear the npm cache
    c.run("npm cache clean --force")


@task(aliases=["i"], pre=[clean], help={"prod": "Install production dependencies."})
def install(c: Context, prod: bool = False) -> None:
    """Install dependencies."""
    if prod:
        c.run("echo 'Installing dependencies ...'")
        c.run("pip install .")
    else:
        c.run("echo 'Installing development dependencies ...'")
        c.run("pip install -e .[dev]")

    # Install the dependencies
    c.run("echo 'Installing npm dependencies ...'")
    c.run("npm install")


@task(aliases=["f"])
def format_code(c: Context) -> None:
    """Format code with black and isort."""
    c.run("echo 'Formatting code ...'")

    # Format code
    c.run("black lambda_kit/ tests/ tasks.py")

    # Sort imports
    c.run("isort lambda_kit/ tests/ tasks.py")


@task(aliases=["l"], pre=[format_code])
def lint(c: Context) -> None:
    """Run linters (flake8 and pylint)."""
    c.run("echo 'Analyzing Syntax ...'")
    c.run("flake8 lambda_kit/ tests/ tasks.py")
    c.run("pylint lambda_kit/ tests/ tasks.py")
    c.run("mypy lambda_kit/ tests/ tasks.py")


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


@task(aliases=["b"])
def build(c: Context) -> None:
    """Build the package."""
    c.run("echo 'Building the package ...'")
    c.run("python -m build")


@task(aliases=["s"])
def semantic_release(c: Context) -> None:
    """Run semantic release."""
    c.run("echo 'Running semantic release ...'")
    c.run("rm -rf node_modules")
    c.run("npm install")
    c.run("npx semantic-release")


@task(aliases="r", pre=[clean, build])
def release(c: Context) -> None:
    """Release the package to PyPI."""
    c.run("echo 'Releasing the package ...'")
    c.run("twine upload dist/*")


# Create a collection and set the default task
ns = Collection(
    clean,
    install,
    lint,
    test,
    build,
    semantic_release,
    format_code,
    package,
    run_all_tasks,
)
ns.configure({"run": {"echo": True}})
ns.default = "run_all_tasks"
