# Program to convert number grades (0 -100) to letter grades (F-A)
# Author: Chris Williams

def studentGrade(score):
    # Create grade scale
    grade = "F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A" * 10

    # Return associated letter grade
    return grade[score]

def main():
    print(studentGrade(95))
main()
    
