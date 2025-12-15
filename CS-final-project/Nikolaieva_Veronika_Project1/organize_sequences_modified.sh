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

# Step 3.1: Create otput dir, where the results of dorting will be stored
OUTPUT_DIR="${INPUT_DIR}_sorted"
# Step 3.2: Create output folders
mkdir -p "$OUTPUT_DIR/small" "$OUTPUT_DIR/medium" "$OUTPUT_DIR/large"

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
        mv "$file" "$OUTPUT_DIR/small/"
        small_count=$((small_count + 1))

    elif [ "$seq_count" -ge 6 ] && [ "$seq_count" -le 10 ]; then
        mv "$file" "$OUTPUT_DIR/medium/"
        medium_count=$((medium_count + 1))

    elif [ "$seq_count" -gt 10 ]; then
        mv "$file" "$OUTPUT_DIR/large/"
        large_count=$((large_count + 1))
    fi

    total_sequences=$((total_sequences + seq_count))
    total_files=$((total_files + 1))
done

# Step 6: Create summary file
# Your code here: write summary.txt
cat > "$OUTPUT_DIR/summary.txt" <<EOF
Total files processed: $total_files
Small category (1-5 sequences): $small_count files
Medium category (6-10 sequences): $medium_count files
Large category (>10 sequences): $large_count files
Total sequences across all files: $total_sequences
EOF
