name = input("What's your name? ").strip().title()
parts = name.split()

#Remove white spaces from str and capitalize
#name = name.strip().title()

#Capitalize the first letter
#name = name.capitalize()
#name = name.title()

#Split user name into main name and lastname
first_name = name.split(" ")[0]
last_name = parts[1] if len(parts) > 1 else ""

#print("Hello", name)
print(f"Hello, {first_name} {last_name}")

# This my first step into Python