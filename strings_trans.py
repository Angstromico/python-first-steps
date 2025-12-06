def main(): 
    string_base = "Hello, World!"
    uppercase_string = string_base.upper()
    lowercase_string = string_base.lower()
    capitalized_string = lowercase_string.capitalize()

    print("Lowercase:", string_base)
    print("Uppercase:", uppercase_string)
    print("Lowercase:", lowercase_string)
    print("Capitalized:", capitalized_string)


if __name__ == "__main__":
    main()
