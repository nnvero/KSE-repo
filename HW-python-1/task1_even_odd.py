def check_even_odd(number):
    """
    Check if a number is even or odd.
    Returns: "even" or "odd"
    """
    DIVISOR = 2

    # Checking the data type of the input
    if type(number) == int or type(number) == float:
        
        # Checking is there is remainder after the modulo operation
        remainder = number % DIVISOR
        if remainder == 0:
            return "Even"
        else:
            return "Odd"
    
    else:
        return "Function takes only numbers as args."


# print(check_even_odd("a"))
# print(check_even_odd(8.5))
# print(check_even_odd(7))
# print(check_even_odd(8))

