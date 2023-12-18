#!/bin/bash

# Create a virtual environment
python3 -m venv .venv

# Check if the virtual environment is created successfully
if [ $? -ne 0 ]; then
    echo "Error: Unable to create the virtual environment."
    exit 1
fi

# Activate the virtual environment
source .venv/bin/activate

# Install required dependencies
pip3 install colored

# Check if the dependencies are installed successfully
if [ $? -ne 0 ]; then
    echo "Error: Unable to install dependencies."
    exit 1
fi

# Run the Python application
python3 main.py

