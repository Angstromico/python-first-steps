from generals import is_string, is_valid_number

def ask_name() -> str:
    """Keep asking until we get a valid name."""
    while True:
        name = input("What's your name? ").strip().title()

        if not is_string(name):
            print("❌ Invalid name provided. Please enter text.")
            continue
        if is_valid_number(name):
            print("❌ Name cannot be a number. Try again.")
            continue

        return name

def say_hello(name: str = "Manuel Morales") -> None:
    parts = name.split()
    first_name = parts[0]
    last_name = parts[1] if len(parts) > 1 else ""
    print(f"Hello, {first_name} {last_name}")

def main():
    name = ask_name()
    say_hello(name)
    say_hello()  # default greeting

if __name__ == "__main__":
    main()
