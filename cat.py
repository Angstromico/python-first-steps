import generals
import math

def main():
    meows_generator()

def meows_generator():
    # --- Input Validation Loop ---
    while True:
        total_input = input("How many times should the cat meow? ").strip()
        
        # 1. Validate if it's a non-negative whole number (using the imported function)
        if not generals.is_integer(total_input):
            print(f"'{total_input}' is not a valid whole number. Please enter a positive integer.")
            # If invalid, the loop continues (implicitly via the while True)
            continue
        
        # Now we know it's a valid integer string, convert it
        total = int(total_input)
        
        # 2. Check if the resulting number is positive (>= 1)
        if total <= 0:
            print("Please enter a number greater than zero.")
            # If non-positive, the loop continues
            continue
            
        # If we reach here, input is valid and positive. Exit the infinite loop.
        break

    # --- Pre-calculate the quarter points (improved logic) ---
    
    # We use list comprehension and the ceil function for reliable rounding up,
    # ensuring that 1/4 of 10 (2.5) is marked at 3, not 2.
    # The set() removes duplicates automatically.
    
    quarter_points = {
        math.ceil(total * 0.25),
        math.ceil(total * 0.50),
        math.ceil(total * 0.75),
        total # Always include the final meow
    }
    
    # Optional: Convert to a list and sort for debugging, but set is faster for 'in' check
    # quarter_points = sorted(list(quarter_points), reverse=True) 

    print(f"\n--- Starting Meow Sequence (Total: {total}) ---")

    # --- Meow Loop ---
    # The 'range(total)' provides numbers from 0 up to (total - 1)
    for i in range(total):
        meows_counter = i + 1 # Convert 0-based index to 1-based count

        if meows_counter in quarter_points:
            print(f"{meows_counter}: Meoooooowwwwww!")
        else:
            print(f"{meows_counter}: Meow")


if __name__ == "__main__":
    main()