#!/usr/bin/env zsh

python3 -m pip install --upgrade pip
python3 -m pip install setuptools wheel build invoke
invoke install --dev

