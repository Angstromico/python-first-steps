# Turn data type in Python

def main(): 
    text_number = input("Enter a number: ")
    try:
        number = float(text_number)
        print(f"You entered the number: {number}")
        int_number = int(number)
        print(f"As an integer, that's: {int_number}")
    except ValueError:
        print("That's not a valid number!")


if __name__ == "__main__":
    main()
