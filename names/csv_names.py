import os

def main(): 
    students = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "students.csv")

    with open(file_path, "r") as file:
        for line in file:
            name, house = line.strip().split(",")
            student = {"name": name, "house": house}
            students.append(student)
        
        for student in sorted(students, key=lambda s: s["name"]):
            print(f"{student['name']} from {student['house']}")


if __name__ == "__main__":
    main()
