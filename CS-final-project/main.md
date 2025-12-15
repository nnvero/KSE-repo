# Bioinformatics Programming - Final Projects (Beginner Level)

## Course: Programming Fundamentals 

---

## Project Overview

### 🎯 Learning Goals

These projects will help you practice:
- ✅ Loops (for and while)
- ✅ Conditionals (if/elif/else)
- ✅ Basic data structures (lists and dictionaries)
- ✅ File reading and writing
- ✅ String manipulation
- ✅ Basic BASH commands

**Total Points: 40**
- **Project 1 (BASH):** 10 points
- **Project 2 (Python):** 30 points

---

## Project 1: BASH Scripting (10 points)

### 🎯 Project: "DNA Sequence File Organizer"

### What You'll Build

A simple BASH script that organizes DNA sequence files by counting their sequences and organizing them into folders.

### What You'll Practice

- Reading command line arguments
- Using loops to process files
- Using if statements for decisions
- Basic text processing with grep and wc
- Creating directories and moving files

---

### Requirements

Your script `organize_sequences.sh` should do the following:

#### 1. Accept Input (1 point)

```bash
./organize_sequences.sh input_folder/
```

The script should:
- Check if the folder exists
- Print an error message if it doesn't

#### 2. Count Sequences in Each File (3 points)

For each `.txt` file in the folder:
- Count how many sequences it has (lines starting with `>`)
- Print the filename and count

Example output:
```
sample1.txt: 2 sequences
sample2.txt: 5 sequences
sample3.txt: 1 sequences
```

#### 3. Organize Files by Size (4 points)

Create three folders and move files based on sequence count:
- `small/` - files with 1-5 sequences
- `medium/` - files with 6-10 sequences  
- `large/` - files with more than 10 sequences

#### 4. Create a Summary (2 points)

Create a file `summary.txt` with:
- Total number of files processed
- Number of files in each category
- Total sequences across all files

---

### Test Data Provided

**Download the `samples_part_1.zip` file from Moodle** which contains 10 test files:

| File | Sequences | Expected Category |
|------|-----------|-------------------|
| sample1.txt | 2 | small |
| sample2.txt | 5 | small (boundary case) |
| sample3.txt | 1 | small |
| sample4.txt | 7 | medium |
| sample5.txt | 10 | medium (boundary case) |
| sample6.txt | 6 | medium (boundary case) |
| sample7.txt | 12 | large |
| sample8.txt | 15 | large |
| sample9.txt | 20 | large |
| sample10.txt | 4 | small |

**Total: 82 sequences across 10 files**

### How to Use Test Data

1. Download and extract `samples_part_1.zip`
2. Create a folder for testing:
   ```bash
   mkdir test_sequences
   cd test_sequences
   # Copy all sample*.txt files here
   ```
3. Run your script:
   ```bash
   ./organize_sequences.sh test_sequences/
   ```

### Expected Results

After running your script successfully, you should have:

```
test_sequences/
├── small/
│   ├── sample1.txt (2 sequences)
│   ├── sample2.txt (5 sequences)
│   ├── sample3.txt (1 sequence)
│   └── sample10.txt (4 sequences)
├── medium/
│   ├── sample4.txt (7 sequences)
│   ├── sample5.txt (10 sequences)
│   └── sample6.txt (6 sequences)
├── large/
│   ├── sample7.txt (12 sequences)
│   ├── sample8.txt (15 sequences)
│   └── sample9.txt (20 sequences)
└── summary.txt
```

**summary.txt should contain:**
```
Total files processed: 10
Small category (1-5 sequences): 4 files
Medium category (6-10 sequences): 3 files
Large category (>10 sequences): 3 files
Total sequences across all files: 82
```

---

### Example Input File Format

All sample files use FASTA format. Here's what **sample1.txt** looks like:

```
>sequence_1_sample1
ATCGATCGATCGATCG
>sequence_2_sample1
GCTAGCTAGCTAGCTA
```

The `>` symbol marks the beginning of a sequence header. This file has **2 sequences**, so it should go in the `small/` folder.

---

### Step-by-Step Guide

```bash
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
    # Your code here:
    # - Count sequences (lines with >)
    # - Determine which folder to use
    # - Move the file
    # - Update counters
done

# Step 6: Create summary file
# Your code here: write summary.txt
```

---

### Tips for Counting Sequences

To count sequences (lines starting with `>`), use:
```bash
seq_count=$(grep -c "^>" "$file")
```

The `^` symbol means "start of line", so this only counts lines that **begin** with `>`.

---

### Grading Rubric - Project 1

| Criteria | Points | What We're Looking For |
|----------|--------|------------------------|
| **Input handling** | 1 | Checks arguments and folder existence |
| **Counting sequences** | 3 | Correctly counts > symbols in each file |
| **File organization** | 4 | Moves files to correct folders based on count |
| **Summary creation** | 2 | Creates summary.txt with all required info |
| **TOTAL** | **10** | |

---

### What to Submit

```
LastName_FirstName_Project1.zip
├── organize_sequences.sh      # Your script
├── README.md                  # How to run it
├── test_output/               # Results from running on test data
│   ├── small/
│   │   ├── sample1.txt
│   │   ├── sample2.txt
│   │   ├── sample3.txt
│   │   └── sample10.txt
│   ├── medium/
│   │   ├── sample4.txt
│   │   ├── sample5.txt
│   │   └── sample6.txt
│   ├── large/
│   │   ├── sample7.txt
│   │   ├── sample8.txt
│   │   └── sample9.txt
│   └── summary.txt
└── data/                      # Original test files (copy of samples)
    ├── sample1.txt
    ├── sample2.txt
    ├── ...
    └── sample10.txt
```

---

## Project 2: Python Programming (30 points)

### 🎯 Project: "DNA Sequence Analyzer"

### What You'll Build

A Python program that reads DNA sequences from a file and calculates basic statistics about them.

### What You'll Practice

- Reading files line by line
- Using for loops to process data
- Using if/elif/else for decisions
- Working with lists and dictionaries
- Counting and calculating percentages
- Writing results to files

---

### Part A: Basic Functions (15 points)

#### Function 1: Count Nucleotides (3 points)

```python
def count_nucleotides(sequence):
    """
    Count how many A, T, G, C are in a DNA sequence.
    
    Example:
    >>> count_nucleotides("ATCGATCG")
    {'A': 2, 'T': 2, 'G': 2, 'C': 2}
    """
    # Your code here:
    # 1. Create a dictionary with counts for A, T, G, C (all starting at 0)
    # 2. Loop through each letter in the sequence
    # 3. For each letter, add 1 to its count
    # 4. Return the dictionary
```

**Requirements:**
- Create a dictionary with keys 'A', 'T', 'G', 'C'
- Use a for loop to go through the sequence
- Count each nucleotide
- Return the dictionary

---

#### Function 2: Calculate GC Content (3 points)

```python
def calculate_gc_content(sequence):
    """
    Calculate what percentage of the sequence is G or C.
    
    Example:
    >>> calculate_gc_content("ATCGATCG")
    50.0
    """
    # Your code here:
    # 1. Count how many G's and C's
    # 2. Calculate total length
    # 3. Calculate percentage: (G+C) / total * 100
    # 4. Return the percentage
```

**Requirements:**
- Count G and C letters
- Calculate percentage
- Return a number (float)

**Hint:** You can use `count_nucleotides()` to help!

---

#### Function 3: Find Complement (3 points)

```python
def find_complement(sequence):
    """
    Find the complement of a DNA sequence.
    A ↔ T, G ↔ C
    
    Example:
    >>> find_complement("ATCG")
    "TAGC"
    """
    # Your code here:
    # 1. Create empty string for result
    # 2. Loop through each letter
    # 3. For each letter, add its complement to result
    #    - If A, add T
    #    - If T, add A
    #    - If G, add C
    #    - If C, add G
    # 4. Return result string
```

**Requirements:**
- Use a for loop
- Use if/elif statements for each nucleotide
- Build the complement string letter by letter
- Return the complement

---

#### Function 4: Check Valid DNA (3 points)

```python
def is_valid_dna(sequence):
    """
    Check if a sequence contains only A, T, G, C.
    
    Example:
    >>> is_valid_dna("ATCG")
    True
    >>> is_valid_dna("ATXG")
    False
    """
    # Your code here:
    # 1. Loop through each letter in sequence
    # 2. If any letter is not A, T, G, or C, return False
    # 3. If you finish the loop without finding bad letters, return True
```

**Requirements:**
- Loop through the sequence
- Check each letter
- Return True or False

---

#### Function 5: Find All Sequences (3 points)

```python
def read_sequences_from_file(filename):
    """
    Read DNA sequences from a file.
    Format: Each line is one sequence
    
    Returns:
    List of sequences (as strings)
    """
    # Your code here:
    # 1. Create empty list
    # 2. Open the file
    # 3. Loop through each line
    # 4. Remove whitespace (strip)
    # 5. If line is not empty, add to list
    # 6. Return the list
```

**Requirements:**
- Open file and read it
- Use a for loop for lines
- Create a list of sequences
- Remove extra spaces/newlines

**Example file (sequences.txt):**
```
ATCGATCG
GCTAGCTA
TTAATTAA
```

---

### Part B: Main Program (10 points)

#### Create `analyzer.py`

```python
"""
DNA Sequence Analyzer
Reads sequences from a file and calculates statistics.
"""

# Put all your functions here (from Part A)

def main():
    """Main program"""
    
    # 1. Ask user for filename
    filename = input("Enter filename: ")
    
    # 2. Read all sequences from file
    sequences = read_sequences_from_file(filename)
    
    # 3. Check if file had any sequences
    if len(sequences) == 0:
        print("Error: No sequences found in file!")
        return
    
    # 4. Analyze each sequence
    print(f"\nAnalyzing {len(sequences)} sequences...\n")
    
    for i, sequence in enumerate(sequences, 1):
        print(f"Sequence {i}: {sequence}")
        
        # Check if valid
        if not is_valid_dna(sequence):
            print("  ERROR: Invalid DNA sequence!")
            continue
        
        # Calculate statistics
        counts = count_nucleotides(sequence)
        gc = calculate_gc_content(sequence)
        complement = find_complement(sequence)
        
        # Print results
        print(f"  Length: {len(sequence)}")
        print(f"  A: {counts['A']}, T: {counts['T']}, G: {counts['G']}, C: {counts['C']}")
        print(f"  GC content: {gc:.1f}%")
        print(f"  Complement: {complement}")
        print()
    
    # 5. Calculate summary statistics
    total_sequences = len(sequences)
    avg_length = sum(len(seq) for seq in sequences) / total_sequences
    
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total sequences: {total_sequences}")
    print(f"Average length: {avg_length:.1f}")
    
    # 6. Save results to file
    with open("results.txt", "w") as f:
        f.write("DNA Sequence Analysis Results\n")
        f.write("=" * 50 + "\n")
        f.write(f"Total sequences analyzed: {total_sequences}\n")
        f.write(f"Average length: {avg_length:.1f}\n")

# Run the program
if __name__ == "__main__":
    main()
```

**Requirements:**
- Read filename from user
- Process each sequence
- Print statistics for each
- Calculate and print summary
- Save results to file

---

### Part C: Additional Feature (5 points)

**Choose ONE of these to implement:**

#### Option 1: Find the longest sequence

```python
def find_longest_sequence(sequences):
    """Return the longest sequence from a list"""
    # Hint: Keep track of longest so far while looping
```

#### Option 2: Count AT-rich sequences

```python
def count_at_rich(sequences):
    """Count how many sequences have more than 60% A+T"""
    # Hint: Use calculate_gc_content(), if GC < 40%, then AT > 60%
```

#### Option 3: Find repeated sequences

```python
def find_duplicates(sequences):
    """Find sequences that appear more than once"""
    # Hint: Use a dictionary to count occurrences
```

---

### Example Run

```
Enter filename: sequences.txt

Analyzing 3 sequences...

Sequence 1: ATCGATCG
  Length: 8
  A: 2, T: 2, G: 2, C: 2
  GC content: 50.0%
  Complement: TAGCTAGC

Sequence 2: GCTAGCTA
  Length: 8
  A: 2, T: 2, G: 2, C: 2
  GC content: 50.0%
  Complement: CGATCGAT

Sequence 3: TTAATTAA
  Length: 8
  A: 4, T: 4, G: 0, C: 0
  GC content: 0.0%
  Complement: AATTAATT

==================================================
SUMMARY
==================================================
Total sequences: 3
Average length: 8.0

Results saved to results.txt
```

---

### Grading Rubric - Project 2

| Part | Criteria | Points | What We're Looking For |
|------|----------|--------|------------------------|
| **A** | **Basic Functions** | **15** | |
| | count_nucleotides() | 3 | Uses loop and dictionary |
| | calculate_gc_content() | 3 | Calculates percentage correctly |
| | find_complement() | 3 | Uses if/elif for each nucleotide |
| | is_valid_dna() | 3 | Checks all letters |
| | read_sequences_from_file() | 3 | Reads file into list |
| **B** | **Main Program** | **10** | |
| | User input | 1 | Gets filename from user |
| | Read file | 1 | Calls read function |
| | Loop through sequences | 2 | Processes each sequence |
| | Calculate & print stats | 3 | Shows all required info |
| | Summary statistics | 2 | Calculates totals/averages |
| | Save to file | 1 | Writes results.txt |
| **C** | **Additional Feature** | **5** | |
| | Implementation | 3 | Feature works correctly |
| | Integration | 2 | Added to main program |
| **TOTAL** | | **30** | |

---

### What to Submit

```
LastName_FirstName_Project2.zip
├── analyzer.py                # Your main program
├── README.md                  # How to run it
├── test_sequences.txt         # Test file you used
└── results.txt                # Output from running your program
```

---

## Simplified Submission Guide

### Project 1 Checklist

- [ ] Downloaded and extracted `samples_part_2.zip` from Moodle
- [ ] My script takes one argument (the folder path)
- [ ] It checks if the folder exists
- [ ] It counts sequences in each file correctly
- [ ] It creates small/medium/large folders
- [ ] It moves files to the right folder
- [ ] It creates summary.txt with correct totals (10 files, 82 sequences)
- [ ] I included a README explaining how to run it
- [ ] I tested it with the provided sample files
- [ ] My test_output shows 4 small, 3 medium, 3 large files

### Project 2 Checklist

- [ ] Function 1 (count_nucleotides) works
- [ ] Function 2 (calculate_gc_content) works
- [ ] Function 3 (find_complement) works
- [ ] Function 4 (is_valid_dna) works
- [ ] Function 5 (read_sequences_from_file) works
- [ ] Main program runs without errors
- [ ] Program prints results to screen
- [ ] Program saves results.txt
- [ ] I added one additional feature
- [ ] I included a README with instructions
- [ ] I tested it with different input files

---

## Tips for Success

### BASH Project

✅ **DO:**
- Test with the provided sample files first
- Use `echo` to see what's happening
- Start with just one test file
- Use `grep -c "^>"` to count sequences
- Verify your output matches expected results

❌ **DON'T:**
- Try to do everything at once
- Forget to check if folder exists
- Count blank lines instead of sequences

### Python Project

✅ **DO:**
- Test each function individually
- Use simple inputs first (like "ATCG")
- Print values to see if they're correct
- Start with just one sequence
- Add features one at a time

❌ **DON'T:**
- Write all code without testing
- Use complicated test data first
- Forget to save your file before running
- Skip the basic functions

---

## Common Mistakes & Solutions

### BASH

**Mistake:** Script says "command not found"
```bash
# Solution: Make it executable
chmod +x organize_sequences.sh
```

**Mistake:** Can't find files
```bash
# Solution: Check you're using the right path
ls "$INPUT_DIR"/*.txt  # See what files are there
```

**Mistake:** Wrong sequence count
```bash
# Problem: Counting all lines instead of just headers
wc -l file.txt  # WRONG - counts all lines

# Solution: Count only lines starting with >
grep -c "^>" file.txt  # CORRECT - counts sequences
```

**Mistake:** Variables not working
```bash
# Solution: Use quotes around variables
mv "$file" "$destination"  # Good
mv $file $destination       # Bad (breaks with spaces)
```

### Python

**Mistake:** `KeyError: 'A'`
```python
# Solution: Initialize your dictionary first
counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
```

**Mistake:** `TypeError: unsupported operand type(s)`
```python
# Solution: Make sure you're using numbers
percentage = (count / total) * 100  # Make sure count and total are int/float
```

**Mistake:** File not found
```python
# Solution: Check the filename is correct
import os
print(os.getcwd())  # See where you are
print(os.listdir())  # See what files are here
```

---

## Test Data Information

### For Project 1 (BASH)

**Download:** `samples.zip` from Moodle

**Contains:** 10 DNA sequence files in FASTA format

**Expected Results When Script Runs Correctly:**
- Total files processed: 10
- Small category: 4 files (sample1, sample2, sample3, sample10)
- Medium category: 3 files (sample4, sample5, sample6)
- Large category: 3 files (sample7, sample8, sample9)
- Total sequences: 82

**Important Boundary Cases to Test:**
- sample2.txt has exactly 5 sequences (should be "small", NOT "medium")
- sample6.txt has exactly 6 sequences (should be "medium", NOT "small")
- sample5.txt has exactly 10 sequences (should be "medium", NOT "large")

### For Project 2 (Python)

Create your own test file `test_sequences.txt` with simple DNA sequences like:
```
ATCGATCG
GCTAGCTA
TTAATTAA
```

---

## Grading Summary

| Project | Points | Focus |
|---------|--------|-------|
| BASH (Project 1) | 10 | Loops, conditionals, file operations |
| Python (Project 2) | 30 | Functions, loops, dictionaries, file I/O |
| **TOTAL** | **40** | Basic programming skills |

---

## Academic Integrity

### ✅ You CAN:
- Use course notes and slides
- Ask instructor/TA for help
- Look up basic syntax (how to read a file, etc.)
- Discuss ideas with classmates

### ❌ You CANNOT:
- Copy code from other students
- Copy complete solutions from internet
- Have someone else write your code
- Share your code with others

### AI Tools (ChatGPT, etc.)
- You can use AI to **explain concepts**
- You cannot use AI to **write your functions**
- You must **understand all code** you submit
- If you use AI for help, add a comment: `# Asked ChatGPT about syntax`

**Penalty for cheating:** 0 points + possible course failure

---

## FAQs

**Q: Can I use different function names?**
A: No, please use the exact function names we provided. Our tests depend on them.

**Q: What if my code doesn't work perfectly?**
A: Submit what you have! Partial credit is better than nothing.

**Q: Can I add extra features?**
A: Yes! Extra features can earn bonus points.

**Q: My BASH script gives different counts than expected. What's wrong?**
A: Make sure you're counting lines that START with `>` (use `grep -c "^>"`), not all lines.

**Q: How do I test if my functions work?**
A: Add test code at the bottom of your file:
```python
# Test your functions
print(count_nucleotides("ATCG"))  # Should print {'A': 1, 'T': 1, 'G': 1, 'C': 1}
print(calculate_gc_content("ATCG"))  # Should print 50.0
```

**Q: What Python version?**
A: Python 3.8 or newer (any 3.x should work)

**Q: Can I make my program fancier?**
A: Sure, but make sure the basic requirements work first!

**Q: Where do I download the test files?**
A: Download `samples_part_1/2.zip` from Moodle. It contains all 10 sample files you need for testing.

---

## Good Luck! 🚀

Remember:
- Start early
- Test frequently with the provided samples
- Ask for help when stuck
- Read the requirements carefully
- Verify your results match the expected output

**The goal is to learn, not just to get points. Take your time and understand what you're doing!**