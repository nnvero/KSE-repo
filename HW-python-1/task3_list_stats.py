def calculate_stats(numbers):
    """
    Calculate min, max, and average from a list of numbers.
    Returns: dictionary with keys 'min', 'max', 'average'
    """
    # Sorting numbers in ascending order
    numbers_sorted = sorted(numbers)    

    # Getting min number from sorted list
    min_number = numbers_sorted[0]
    # Getting ma[] number from sorted list
    max_number = numbers_sorted[-1]


    numbers_sum = sum(numbers)
    numbers_count = len(numbers)
    # Getting average
    average = numbers_sum/numbers_count

    return {'min': min_number, 'max': max_number, 'average': average}

    

result = calculate_stats([10, 20, 30, 40, 50])
print(result)  # {'min': 10, 'max': 50, 'average': 30.0}