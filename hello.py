def main():
    name = input("What's your name? ")
    say_hello(name)
    say_hello()

#name = input("What's your name? ").strip().title()

#Remove white spaces from str and capitalize
#name = name.strip().title()

#Capitalize the first letter
#name = name.capitalize()
#name = name.title()

# say_hello(name)
# say_hello()

def say_hello(name="Manuel Morales"):
    parts = name.split() 
    #Split user name into main name and lastname
    first_name = name.split(" ")[0]
    last_name = parts[1] if len(parts) > 1 else ""
    #print("Hello", name)
    print(f"Hello, {first_name} {last_name}")

main()

# This my first step into Python