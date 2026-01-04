from hello_test import hello

def check_string(name):
    return is_string(name)

def is_string(s: str) -> bool:
    """Checks if a string is a string."""
    return isinstance(s, str) and len(s) > 0

def test_hello():
    assert hello("Alice") == "Hello, Alice!"
    assert hello() == "Hello, World!"

def test_check_if_string_hello():
    assert check_string(hello("Bob")) == True
    assert check_string(hello(5)) == True
    assert check_string(hello(None)) == True
