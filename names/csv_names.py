import os
import csv

def main(): 
    students = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "students.csv")

    with open(file_path, "r") as file:
        reader = csv.DictReader(file, fieldnames=["name", "home", "country"])
        next(reader)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"], "country": row["country"]})
        
        for student in sorted(students, key=lambda s: s["name"]):
            if student["country"]:
                print(f"{student['name']} from {student['home']} in {student['country']}")
            else:
                print(f"{student['name']} from {student['home']}")


if __name__ == "__main__":
    main()
