#!/bin/bash
# Exit immediately if a command fails
set -e  
echo "Running the EZ Diffusion Model Pipeline 3000 times..."

# Run simulate.py 3000 times
for i in {1..3000}; do
    echo "Iteration: $i"
    python3 src/simulate.py
done

echo "Pipeline completed! Results saved in recovered_parameters.csv"
