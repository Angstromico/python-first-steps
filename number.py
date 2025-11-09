def main(): 
    value = get_interger("Enter a integer number please: ")
    # while True:
    #     try:
    #         x = input("Enter an integer: ")
    #         value = int(x)
    #         break
    #     except: 
    #         print(f"Invalid input: {x} is not an integer")
        # else: 
        #     break

    print(f"{value} is an integer") #Why tjis is working fine, is not value only lives in the scope of the while?
    # x = input("Enter an integer: ")
    # value = x
    # try: 
    #     x = input("Enter an integer: ")
    #     value = int(x)
    # except ValueError:
    #     print(f"Invalid input: {x} is not an integer")
    # else: 
    #     print(f"{x} is an integer")

    #print(f"x is {(value)}")

def get_interger(question = "Enter an integer: "):
    while True:
        try:
            #return int(input("Enter an integer: "))
            return int(input(question))
            # x = input("Enter an integer: ")
            # value = int(x)
            # return value
        except:
            pass 
            #print("Invalid input")
            #print(f"Invalid input: {x} is not an integer")


if __name__ == "__main__":
    main()
