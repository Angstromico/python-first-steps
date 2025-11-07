import compare

def main():
  score = input("Enter your score: ")

  if not compare.is_valid_number(score):
    print("Invalid score")
    return
  
  if not is_valid_score(score):
    print("Invalid score")
    return
  
  score = float(score)
  
  if score >= 90:
    print("Grade: A")
  elif score >= 80:
    print("Grade: B")
  elif score >= 70:
    print("Grade: C")
  elif score >= 60:
    print("Grade: D")
  else:
    print("Grade: F")
  
def is_valid_score(score):
  try:
    score = float(score)
    if score < 0 or score > 100:
      return False
    return True
  except ValueError:
    return False 

main()