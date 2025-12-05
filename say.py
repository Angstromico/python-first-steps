from sayings import hello, goodbye
from generals import is_string
import sys

def main(): 
    name = input("Enter your name: ")

    if is_string(name.strip()) == False:
        sys.exit("No name provided.")
    
    hello(name.strip())
    goodbye(name.strip())



if __name__ == "__main__":
    main()
