def main(): 
    # Generate random ID with the name, lastname date and four random digits from user inputs
    from random import randint

    name = input("Enter your name: ").strip().title().upper()
    lastname = input("Enter your lastname: ").strip().title().upper()
    date = input("Enter the year of birth: ").strip()
    last_date_two_digits = date[-2:] if len(date) >= 2 else date.zfill(2)
    random_digits = f"{randint(0, 9999):04d}" # Four random digits with leading zeros
    random_id = f"{name[:2]}{lastname[:2]}{last_date_two_digits}{random_digits}"
    print(f"Your random ID is: {random_id}")

if __name__ == "__main__":
    main()
