import csv
from generals import is_valid_number, text_to_number


CAREERS = [
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil Engineering",
    "Computer Engineering",
    "Industrial Engineering"
]


def main():
    # Ask how many pupils
    while True:
        n = input("How many pupils? ")

        if not is_valid_number(n):
            print("Error: please enter a valid number.")
            continue

        n = int(text_to_number(n))
        if n <= 0:
            print("Error: number must be greater than 0.")
            continue

        break

    # Write pupils to CSV
    with open("pupils.csv", "a", newline="") as file:
        writer = csv.writer(file)

        for _ in range(n):
            name = input("Pupil full name: ").strip()

            # Career selection
            while True:
                print("\nChoose a career:")
                for i, career in enumerate(CAREERS, start=1):
                    print(f"{i}. {career}")

                option = input("Option number: ")

                if not is_valid_number(option):
                    print("Error: choose a valid option number.")
                    continue

                option = int(text_to_number(option))
                if option < 1 or option > len(CAREERS):
                    print("Error: option out of range.")
                    continue

                career = CAREERS[option - 1]
                break

            writer.writerow([name, career])
            print("Pupil saved!\n")

    # Read pupils from CSV
    print("\n📋 Pupils list:")
    with open("pupils.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"- {row[0]} — {row[1]}")


if __name__ == "__main__":
    main()
