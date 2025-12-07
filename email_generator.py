from generals import is_string

def main(): 
    full_name = input("Enter your full name: ")
    email_domain = input("Enter your email domain (e.g., example.com): ")

    if not is_string(full_name) or not is_string(email_domain):
        print("Invalid input. Please enter valid strings for name and domain.")
        return
    
    email_address = full_name.strip().replace(" ", ".").lower() + "@" + email_domain.lower() + '.com'

    print("Generated email address:", email_address)


if __name__ == "__main__":
    main()
