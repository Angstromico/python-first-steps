def is_valid_number(s: str) -> bool:
    """Checks if a string can be successfully converted to a float."""
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def main():
   x = input("What's x?")
   y = input("What's y?")

   if not is_valid_number(x) or not is_valid_number(y):
    print("Please enter valid numbers for both inputs.")
    exit(1)

   #if x < y or x > y:
   if x != y:
    print("x and y are not equal")

   if float(x) == float(y):
    print(f"{x} is equal to {y}")

   elif float(x) < float(y):
    print(f"{x} is less than {y}")

   else:
    print(f"{x} is greater than {y}")


main()