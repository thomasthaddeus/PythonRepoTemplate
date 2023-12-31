#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define the test command here
TEST_COMMAND="pytest"

# Run the tests
echo "Running tests..."
$TEST_COMMAND

# Check the exit status of the test command
if [ $? -eq 0 ]; then
  echo "Tests passed successfully."
else
  echo "Tests failed."
  exit 1
fi
