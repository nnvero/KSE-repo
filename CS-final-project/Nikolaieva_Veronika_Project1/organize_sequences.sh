#!/bin/bash

# Step 1: Check if argument was provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide input folder"
    echo "Usage: ./organize_sequences.sh input_folder/"
    exit 1
fi

# Step 2: Check if folder exists
INPUT_DIR="$1"
if [ ! -d "$INPUT_DIR" ]; then
    echo "Error: Folder $INPUT_DIR does not exist"
    exit 1
fi

# Step 3: Create output folders
mkdir -p small medium large

# Step 4: Initialize counters
total_files=0
small_count=0
medium_count=0
large_count=0
total_sequences=0

# Step 5: Loop through all .txt files
for file in "$INPUT_DIR"/*.txt; do
    # - Count sequences (lines with >)
    seq_count=$(grep -c "^>" "$file")
    # - Determine which folder to use
    # - Move the file
    # - Update counters
    if [ "$seq_count" -ge 1 ] && [ "$seq_count" -le 5 ]; then
        mv "$file" small/
        small_count=$((small_count + 1))

    elif [ "$seq_count" -ge 6 ] && [ "$seq_count" -le 10 ]; then
        mv "$file" medium/
        medium_count=$((medium_count + 1))

    elif [ "$seq_count" -gt 10 ]; then
        mv "$file" large/
        large_count=$((large_count + 1))
    fi

    total_sequences=$((total_sequences + seq_count))
    total_files=$((total_files + 1))
done

# Step 6: Create summary file
# Your code here: write summary.txt
cat > summary.txt <<EOF
Total files processed: $total_files
Small category (1-5 sequences): $small_count files
Medium category (6-10 sequences): $medium_count files
Large category (>10 sequences): $large_count files
Total sequences across all files: $total_sequences
EOF
