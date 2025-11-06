def get_valid_number(prompt):
    """Continuously prompts the user until a valid integer is entered."""
    while True:
        user_input = input(prompt)
        try:
            # Attempt to convert the input to an float
            number = float(user_input)
            # If successful, break the loop and return the number
            return number
        except ValueError:
            # If conversion fails (because it's a string/text), catch the error
            print(f"'{user_input}' is not a valid number. Please enter a number.")
            # The loop continues, prompting the user again

def clean_float(value: float) -> int | float:
    """
    Checks if a float has no decimal part.
    If the float is equivalent to an integer (e.g., 1.0, 5.0), 
    it returns the integer version (e.g., 1, 5).
    Otherwise (e.g., 1.5, 2.3), it returns the original float.
    """
    # 1. Check if the float is mathematically equal to its integer version.
    #    The int(value) truncates the decimal part (e.g., 1.5 -> 1, 1.0 -> 1).
    #    If the float minus its integer part is 0, it has no decimal.
    if value == int(value):
        # 2. If true, cast the float to an integer and return it.
        return int(value)
    else:
        # 3. If false, return the original float value rounded.
        return round(value, 2)

# Get the first valid number
x = get_valid_number("Enter the first number: ")

# Get the second valid number
y = get_valid_number("Enter the second number: ")

# Calculate the sum
z = clean_float(x + y)

x_to_print = clean_float(x)
y_to_print = clean_float(y)

division = clean_float(x / y)

print(f"\nThe sum of {x_to_print:,} and {y_to_print:,} is {z:,}")
print(f"\nThe division of {x_to_print:,} and {y_to_print:,} is {division:,}")