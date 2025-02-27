#!/bin/bash

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../" && pwd)"

SEEDER_DIRS=("domains")

# Function to run a seeder
run_seeder() {
    seeder_file="$1"
    echo "Running seeder: app.$seeder_file"
    python -m "app.$seeder_file"
}

# Loop through the defined directories
for dir in "${SEEDER_DIRS[@]}"; do
    # Find all seeder.py files in the subdirectories
    find "$BASE_DIR/$dir" -type f -name 'seeder.py' | while read -r seeder; do
        # Convert the file path to module path, removing the leading '/'
        module_path="${seeder#$BASE_DIR/}"
        module_path="${module_path//\//.}"
        module_path="${module_path%.py}"  # Remove the .py extension
        run_seeder "$module_path"  # Execute the seeder
    done
done

echo "All seeders have been executed."
