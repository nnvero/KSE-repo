def get_letter_grade(score):
    """
    Convert score to letter grade.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


print(get_letter_grade(95))  # "A"
print(get_letter_grade(82))  # "B"
print(get_letter_grade(55))  # "F"