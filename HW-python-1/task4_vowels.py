def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in text.
    Case-insensitive.
    """
    VOWELS = 'aeiouAEIOU'

    # Checking data type of the input
    if type(text) != str:
        return "Function takes text only"
    else:
        # Keeping track of vowels in the text
        vowels_count = 0
        for letter in text:
            if letter in VOWELS:
                vowels_count += 1
            else:
                continue

    return vowels_count

print(count_vowels(123)) 
print(count_vowels("Hello World"))  # 3
print(count_vowels("Python"))       # 1