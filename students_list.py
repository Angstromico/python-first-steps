import csv

def main(): 
    name = input('Write the Student Name: ')
    home = input('Write the Home of the student: ')

    with open('students.csv', 'a', newline='' ) as file: 
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


if __name__ == "__main__":
    main()
