def filter_long_words(words, min_length):
    """
    Return list of words longer than min_length.
    """
    longer_words = []

    for word in words:
        if len(word) > min_length:
            longer_words.append(word)

    return longer_words



words = ["cat", "elephant", "dog", "butterfly"]
print(filter_long_words(words, 5))  
# ["elephant", "butterfly"]