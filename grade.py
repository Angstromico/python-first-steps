import compare

def main():
    score = input("Enter your score: ")
    
    # Combine validation checks
    if not (compare.is_valid_number(score) and is_valid_score(score)):
        print("Invalid score")
        return
    
    score = float(score)
    grade = get_grade(score)
    print(f"Grade: {grade}")

def is_valid_score(score):
    try:
        score = float(score)
        return 0 <= score <= 100
    except ValueError:
        return False

def get_grade(score):
    """Returns the letter grade for a given score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    main()