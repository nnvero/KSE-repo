
from task1_even_odd import check_even_odd

def sum_even_numbers(start, end):
    """
    Calculates sum of all even numbers from start to end.
    Takes two args as input - start number and end.
    """
    current_number = start
    even_numbers_sum = 0
    
    while current_number <= end:
        if check_even_odd(current_number) == 'Even':
            # Adding number to the sum
            even_numbers_sum += current_number
            # Moving to the next number
            current_number += 1
        else:
            # Moving to the next number
            current_number += 1

    return even_numbers_sum            

print(sum_even_numbers(1, 10))   # 30 (2+4+6+8+10)
print(sum_even_numbers(5, 15))   # 50 (6+8+10+12+14)   