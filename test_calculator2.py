import pytest
from calculator2 import square

def main():
    test_positives_square_numbers()
    test_negatives_square_numbers()
    test_zero_square_number()

def test_positives_square_numbers():
    assert square(2) == 4 
    assert square(3) == 9

def test_negatives_square_numbers():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero_square_number():
    assert square(0) == 0

def test_str_square_number():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()

