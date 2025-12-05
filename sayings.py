from generals import is_string

def main(): 
    name = input("Enter your name: ")

    if is_string(name.strip()) == False:
        print("No name provided.")
        return
    
    hello(name.strip())
    goodbye(name.strip())

def hello(name):
    print(f"Hello {name}!")

def goodbye(name):
    print(f"Goodbye {name}!")


if __name__ == "__main__":
    main()
