def count_word_frequency(words):
    """
    Count frequency of each word in the list.
    Returns: dictionary with word as key and count as value
    """
    word_frequencies = {}

    for word in words:
        if word not in word_frequencies:
            word_frequencies[word]=1
        else:
            word_frequencies[word]+=1
    
    return word_frequencies


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(count_word_frequency(words))
# {"apple": 3, "banana": 2, "cherry": 1}