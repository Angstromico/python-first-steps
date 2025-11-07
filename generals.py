def is_valid_number(s: str) -> bool:
    """Checks if a string can be successfully converted to a float."""
    try:
        float(s)
        return True
    except ValueError:
        return False