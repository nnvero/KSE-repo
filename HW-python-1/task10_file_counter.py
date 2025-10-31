def count_words_in_file(filename):
    """
    Count total number of words in a file.
    Handle FileNotFoundError - return 0 if file doesn't exist.
    """

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        if len(content) > 0:
            words = content.split(" ")
            word_count = len(words)
        else:
            word_count = 0

    return word_count



# If file contains: "Hello world from Python"
print(count_words_in_file("sample.txt"))  # 4
print(count_words_in_file("missing.txt")) # 0