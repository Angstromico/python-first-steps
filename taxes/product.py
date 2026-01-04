def get_valid_float(prompt: str, allow_negative: bool = False, percentage: bool = False) -> float:
    """Prompt until the user enters a valid float."""
    while True:
        value_input = input(prompt).strip()
        try:
            value = float(value_input)
            if not allow_negative and value < 0:
                print("❌ Value cannot be negative. Try again.")
                continue
            if percentage:
                value /= 100
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

def main(): 
    price = get_valid_float("Enter the product price: ")
    tax_rate = get_valid_float("Enter the tax rate (as a percentage): ", percentage=True)

    total_price = price + (price * tax_rate)
    print(f"The total price including tax is: ${total_price:.2f}")

if __name__ == "__main__":
    main()
