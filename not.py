def main(): 
    # Using the not operator 
    is_raining = False
    if not is_raining:
        print("It's not raining. You can go outside!")
    else:
        print("It's raining. Better stay indoors.")
    
    # Using not with multiple conditions
    is_weekend = True
    if not is_raining and is_weekend:
        print("It's a great day for outdoor activities!")
    else:
        print("Maybe it's better to stay indoors or find indoor activities.")


if __name__ == "__main__":
    main()
