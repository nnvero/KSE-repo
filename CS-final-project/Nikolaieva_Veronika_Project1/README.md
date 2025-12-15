# README

This folder contains **two Bash scripts**: `organize_sequences.sh` and `organize_sequences_modified.sh`.

- `organize_sequences.sh` follows the original instructions given in the assignment: it organizes files into folders, sorting them by the number of sequences they contain (`small`, `medium`, `large`).
**Output folder:** `test_output/`

- `organize_sequences_modified.sh` contains only one modification: it creates an additional folder named `INPUT_DIR+"_sorted"`. The `small`, `medium`, and `large` directories with the corresponding files are then placed inside this additional `INPUT_DIR+"_sorted"` folder.
**Output folder:** `test_output_modified/`

## How to use

./organize_sequences.sh {input_dir}

or

./organize_sequences_modified.sh {input_dir}
