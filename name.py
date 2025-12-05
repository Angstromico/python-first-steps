import sys

def main(): 
    if len(sys.argv) < 3:
        sys.exit("You must provide a first and last name as arguments.")
    try:
        first_name = str(sys.argv[1])
        last_name = str(sys.argv[2])
        print(f"Hello my name is {first_name} {last_name}")

        for arg in sys.argv[1:]: # Print all arguments except the script name
            print(arg)
    except ValueError:
        sys.exit("Both arguments must be strings.")


if __name__ == "__main__":
    main()
