def is_valid_number(s: str) -> bool:
    """Checks if a string can be successfully converted to a float."""
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def is_integer(s: str) -> bool:
    """Checks if a string represents an integer."""
    try:
        int(s)
        return True
    except ValueError:
        return False
    
def is_string(s: str) -> bool:
    """Checks if a string is a string."""
    return isinstance(s, str) and len(s) > 0

def text_to_number(text: str) -> int:
    """Converts a string to a number."""
    if not is_valid_number(text):
        raise ValueError("Invalid number")
    return int(text)