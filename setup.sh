#!/usr/bin/env zsh

# Define the virtual environment directory
VENV_DIR=".venv"

# Remove existing virtual environment
rm -rf $VENV_DIR

# Create a new virtual environment
python3 -m venv $VENV_DIR

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip and install required packages
python3 -m pip install --upgrade pip
python3 -m pip install setuptools wheel build invoke
invoke install
