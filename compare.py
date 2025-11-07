import generals
    
def main():
   x = input("What's x?")
   y = input("What's y?")

   if not generals.is_valid_number(x) or not generals.is_valid_number(y):
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


# ----------------------------------------------------------------
# ONLY RUN main() if this file is the one being executed by the interpreter
# ----------------------------------------------------------------
if __name__ == "__main__":
    main()