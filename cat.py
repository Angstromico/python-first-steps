import generals
import math

def get_valid_positive_integer():
    """Get and validate a positive integer from user input."""
    while True:
        user_input = input("How many times should the cat meow? ").strip()
        
        # Check if it's a valid integer
        if not generals.is_integer(user_input):
            print(f"'{user_input}' is not a valid whole number. Please enter a positive integer.")
            continue
        
        # Convert to integer and check if positive
        number = int(user_input)
        if number <= 0:
            print("Please enter a number greater than zero.")
            continue
            
        return number

def meows_generator(total):
    """Generate meows with special quarter-point meows."""
    # --- Pre-calculate the quarter points (improved logic) ---
    
    # We use list comprehension and the ceil function for reliable rounding up,
    # ensuring that 1/4 of 10 (2.5) is marked at 3, not 2.
    # The set() removes duplicates automatically.
    
    quarter_points = {
        math.ceil(total * 0.25),
        math.ceil(total * 0.50),
        math.ceil(total * 0.75),
        total  # Always include the final meow
    }
    
    print(f"\n--- Starting Meow Sequence (Total: {total}) ---")

    # --- Meow Loop ---
    # The 'range(total)' provides numbers from 0 up to (total - 1)
    for i in range(total):
        meows_counter = i + 1  # Convert 0-based index to 1-based count

        if meows_counter in quarter_points:
            print(f"{meows_counter}: Meoooooowwwwww!")
        else:
            print(f"{meows_counter}: Meow")

def main():
    # Get validated input first
    total_meows = get_valid_positive_integer()
    
    # Then generate meows with the validated number
    meows_generator(total_meows)

if __name__ == "__main__":
    main()