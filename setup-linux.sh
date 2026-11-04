#!/usr/bin/env bash
set -e

# Change to the directory containing this script
cd "$(dirname "$0")"

echo "===================================="
echo " AI with Python - Linux Setup"
echo "===================================="

# Check Python availability
if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: Python 3 is not installed."
  echo "Please install Python 3 and python3-venv."
  exit 1
fi

echo "Python version:"
python3 --version

# Check for requirements.txt
if [ ! -f requirements.txt ]; then
  echo "ERROR: requirements.txt not found."
  exit 1
fi

# Create virtual environment if needed
if [ ! -f .venv/bin/python ]; then
  echo "Creating virtual environment..."

  if ! python3 -m venv .venv; then
    echo "ERROR: Could not create virtual environment."
    echo "On Ubuntu/Debian, install python3-venv."
    exit 1
  fi
fi

# Install required packages
echo "Installing Python packages..."
.venv/bin/python -m pip install -r requirements.txt

# Start JupyterLab
echo "Starting JupyterLab..."
.venv/bin/python -m jupyter lab
