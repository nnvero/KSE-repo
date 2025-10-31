def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: (C × 9/5) + 32
    """
    FAHRENHEIT_SCALE = 9/5
    FAHRENHEIT_OFFSET = 32

    # Checking the data type of the input
    if type(celsius) == int or type(celsius) == float:
        # Caclucating Fahrenheit
        farenheit = (celsius*FAHRENHEIT_SCALE)+FAHRENHEIT_OFFSET
        return farenheit
    
    else:
        return "Function takes only numbers as args."


print(celsius_to_fahrenheit('a'))
print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0