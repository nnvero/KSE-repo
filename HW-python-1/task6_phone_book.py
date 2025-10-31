def find_phone_number(phone_book, name):
    """
    Look up phone number by name.
    Returns phone number or "Not found" if name doesn't exist.
    """
    if name in phone_book:
        return phone_book[name]
    else:
        return "Not found"


phones = {"Alice": "123-456", "Bob": "789-012"}
print(find_phone_number(phones, "Alice"))   # "123-456"
print(find_phone_number(phones, "Charlie")) # "Not found"