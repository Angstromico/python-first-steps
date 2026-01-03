from calculator2 import square

def main():
    test_square()

def test_square():
    # Define test cases as (input, expected_output)
    test_cases = [
        (0, 0),
        (1, 1),
        (2, 4),
        (3, 9),
        (5, 25),
        (-4, 16)
    ]

    for num, expected in test_cases:
        result = square(num)
        if result != expected:
            print(f"❌ Test failed: square({num}) = {result}, expected {expected}")
        else:
            print(f"✅ Test passed: square({num}) = {expected}")

if __name__ == "__main__":
    main()

