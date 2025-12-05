from random import choice, randint, shuffle
import random

def main(): 
    #fruit = random.choice(['apple', 'banana', 'cherry'])
    fruit = choice(['apple', 'banana', 'cherry'])
    print(f"You selected: {fruit}")

    number = random.randint(1, 10)
    print(f"Random number between 1 and 10: {number}")

    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    print(f"The original deck: {cards}")
    random.shuffle(cards)
    print(f"The shuffled deck: {cards}")


if __name__ == "__main__":
    main()
