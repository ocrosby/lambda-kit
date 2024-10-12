# Contributing to Lambda Packager

Thank you for considering contributing to Lambda Packager! Here are the guidelines for setting up your development environment.

## Prerequisites

- Python 3.6 or higher
- `pip` (Python package installer)
- `virtualenv` (optional but recommended)

## Invoke-based Build System

This project uses invoke a the build system to automate common tasks such as testing, linting,
and packaging.  Invoke allows us to define tasks in a tasks.py file and run them from the
command line.

### Setup

To get started all you need to do is to run the setup.sh shell script.

```shell
chmod +x setup.sh
./setup.sh  
```

This will:

- ensure you have a new python3.13 based virtual environment named .venv
- upgrade pip to the latest version
- install the setuptools wheel build and invoke packages
- run the invoke install task to install the package in editable mode along with development dependencies

At this point all you should need to do to get started is to activate the virtual environment and run the invoke tasks.

```shell
source .venv/bin/activate
invoke --list
```

This will list all the available tasks that you can run.

### Available Tasks

Here are some of the common tasks defined in the tasks.py file:

#### **Clean**: Remove all build, test, coverage, and Python artifacts.

```shell
inv c
```

#### **Install**: Install the package in editable mode along with development dependencies.

```shell
inv i
```

#### **Lint**: Run flake8, pylint, and mypy to analyze the code.

```shell
inv l
```

#### **Test**: Run the test suite using pytest.

```shell
inv t
```

#### **Format**: Format the code using black and isort.

```shell
inv f
```

### Running Tasks

You can run tasks using the **invoke** command followed by the tasks name. For example, 
to run the tests you can use:

```shell
invoke test
```

To see a list of availble tasks, you can use:

```shell
invoke --list
```

## Setting Up Your Development Environment

1. **Fork the repository** on GitHub.

2. **Clone your forked repository** to your local machine:

    ```shell
    git clone https://github.com/yourusername/lambda-packager.git
    cd lambda-packager
    ```

3. **Create a virtual environment** (optional but recommended):

    ```shell
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the package in editable mode** along with development dependencies:

    ```shell
    pip install --upgrade pip
    pip install invoke
    invoke install --dev    
    ```

5. **Run the tests** to ensure everything is set up correctly:

    ```shell
    pytest tests/
    ```

## Development Workflow

1. **Create a new branch** for your feature or bugfix:

    ```shell
    git checkout -b my-feature-branch
    ```

2. **Make your changes** and commit them:

    ```shell
    git add .
    git commit -m "Description of my changes"
    ```

3. **Push your changes** to your forked repository:

    ```shell
    git push origin my-feature-branch
    ```

4. **Create a Pull Request** on GitHub.

## Code Style

Please follow the PEP 8 style guide for Python code. You can use tools like `flake8` to check your code for style issues.

## Running Tests

To run the tests, use the following command:

```shell
pytest