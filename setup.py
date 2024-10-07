from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lambda-packager",
    version="0.1.0",
    description="CLI tool for packaging and deploying Python Lambda functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/lambda-packager",
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        # e.g., 'boto3', 'click'
        "click"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "flake8",
            "pylint",
            "black",
            "mypy",
            "isort",
            "invoke",
            "python-semantic-release",
        ],
    },
    entry_points={
        "console_scripts": [
            "lambda-packager=lambda_packager.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
