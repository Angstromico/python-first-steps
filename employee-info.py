def main():
    # Get employee information
    employee_info()

def employee_info():
    name = input("Enter employee name: ").strip().title()
    position = input("Enter employee position: ").strip().title()
    is_boss = input("Is the employee a boss? (yes/no): ").strip().lower()
    if is_boss in ['yes', 'y']:
        position = "Boss"

    # Keep asking until salary is valid
    while True:
        salary_input = input("Enter employee salary: ").strip()
        try:
            salary = float(salary_input)
            break  # exit loop if conversion works
        except ValueError:
            print("❌ Invalid salary input. Please enter a valid number.")

    print("Employee Information:")
    print(f"Name: {name}")
    print(f"Position: {position}")
    print(f"Salary: ${salary:.2f}")

if __name__ == "__main__":
    main()

