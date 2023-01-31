#!/bin/bash

set -e
# check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root"
    exit 1
fi

SCRIPT_NAME=aiy
SCRIPT_FILE=$SCRIPT_NAME.py
# ask the user for the install directory
read -p "Enter the install directory (default: /usr/local/bin): " BIN_DIR
# if the user didn't enter anything, use the default
if [ -z "$BIN_DIR" ]; then
    BIN_DIR=/usr/local/bin
fi


# Create a symlink to the script file in the BIN_DIR
ln -s "$(pwd)/$SCRIPT_FILE" "$BIN_DIR/$SCRIPT_NAME"

# Make the symlink executable
chmod +x "$BIN_DIR/$SCRIPT_NAME"

echo "Successfully installed $SCRIPT_NAME to $BIN_DIR"
