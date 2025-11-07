import generals

def main(): 
    x = input("Enter a number: ")
    if not generals.is_valid_number(x):
        print("Invalid input")
        return
    
    x = float(x)
    print(f"The square of {x} is {x * x}")


if __name__ == "__main__":
    main()
