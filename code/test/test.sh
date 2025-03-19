#!/bin/bash
# Exit immediately if a test fails
set -e  
echo "🧪 Running unit tests..."

# Run all unit tests in the 'test' directory
python3 -m unittest discover -s test
echo "All tests passed!"