"""
DNA Sequence Analyzer
Reads sequences from a file and calculates statistics.
"""

# Put all your functions here (from Part A)
def read_sequences_from_file(filename):
    """
    Read DNA sequences from a file.
    Format: Each line is one sequence
    
    Returns:
    List of sequences (as strings)
    """
    # Your code here:
    # 1. Create empty list
    sequences = []
    # 2. Open the file
    file = open(filename)
    content = file.readlines()

    # 3. Loop through each line
    for line in content:
    # 4. Remove whitespace (strip)
        line = line.strip()
        # Standardize bases, all of them become upper
        line = line.upper()
    # 5. If line is not empty, add to list
        if len(line) > 0:
            sequences.append(line)
    # 6. Return the list
    return sequences

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
    for base in sequence:
    # 2. If any letter is not A, T, G, or C, return False
        if base not in "ATGC":
            return False
    # 3. If you finish the loop without finding bad letters, return True
    return True


def count_nucleotides(sequence):
    """
    Count how many A, T, G, C are in a DNA sequence.
    
    Example:
    >>> count_nucleotides("ATCGATCG")
    {'A': 2, 'T': 2, 'G': 2, 'C': 2}
    """
    # Your code here:
    # 1. Create a dictionary with counts for A, T, G, C (all starting at 0)
    base_counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    # 2. Loop through each letter in the sequence
    for base in sequence:
    # 3. For each letter, add 1 to its count
        if base in base_counts.keys():
            base_counts[base] += 1
    # 4. Return the dictionary
    return base_counts


def calculate_gc_content(sequence):
    """
    Calculate what percentage of the sequence is G or C.
    
    Example:
    >>> calculate_gc_content("ATCGATCG")
    50.0
    """
    # Your code here:
    # 1. Count how many G's and C's
    base_counts = count_nucleotides(sequence)
    gc_count = base_counts['G'] + base_counts['C']
    # 2. Calculate total length
    seq_length = len(sequence)
    # 3. Calculate percentage: (G+C) / total * 100
    gc_percentage = gc_count / seq_length * 100
    # 4. Return the percentage
    return gc_percentage


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
    complement = str()
    # 2. Loop through each letter
    for base in sequence:
    # 3. For each letter, add its complement to result
    #    - If A, add T
        if base == 'A':
            complement += 'T'
    #    - If T, add A
        elif base == 'T':
            complement += 'A'
    #    - If G, add C
        elif base == 'G':
            complement += 'C'
    #    - If C, add G
        elif base == 'C':
            complement += 'G'
        else:
           complement += '-' 

    # 4. Return result string
    return complement

def count_at_rich(sequences):
    """
    Count how many sequences have more than 60% A+T
    Takes a list of sequences, returns integer
    """
    # Hint: Use calculate_gc_content(), if GC < 40%, then AT > 60%
    at_rich_count = 0
    for seq in sequences:
        at_content = 100 - calculate_gc_content(seq)
        if at_content >= 60:
            at_rich_count += 1

    return at_rich_count


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

    # Count AT-rich sequences
    at_rich_sequences = count_at_rich(sequences)
    
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    print(f"Total sequences: {total_sequences}")
    print(f"Average length: {avg_length:.1f}")
    print(f'Number of AT-rich sequences: {at_rich_sequences}')

    
    # 6. Save results to file
    with open("results.txt", "w") as f:
        f.write("DNA Sequence Analysis Results\n")
        f.write("=" * 50 + "\n")
        f.write(f"Total sequences analyzed: {total_sequences}\n")
        f.write(f"Average length: {avg_length:.1f}\n")

# Run the program
if __name__ == "__main__":
    main()