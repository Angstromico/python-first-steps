import generals

def main(): 
    x = input("Enter a number: ")
    if not generals.is_integer(x):
        print("Invalid input")
        return
    
    x = int(x)
    
    print(f"{x} is {check_even_odd(x)}")

def check_even_odd(n: float):
    return 'Even' if n % 2 == 0 else 'Odd'
        



if __name__ == "__main__":
    main()
