from generals import is_valid_number, text_to_number


def main():
    while True:
        n = input("What's range? ")

        if not is_valid_number(n):
            print("Error: please enter a valid number.")
            continue

        n = text_to_number(n)
        if n <= 0:
            print("Error: number must be greater than 0.")
            continue

        break

    # Write names to file
    with open("names.txt", "a") as file: #Use "w" if you want to overwrite
        for _ in range(n):
            name = input("What's your name? ")
            file.write(name + "\n")
            file.close()

    # Read names from file
    with open("names.txt", "r") as file:
        names = [line.strip() for line in file if line.strip()]

    for name in sorted(names):
        print(f"hello, {name}")

    print(f"The full list is: {names}")


if __name__ == "__main__":
    main()

