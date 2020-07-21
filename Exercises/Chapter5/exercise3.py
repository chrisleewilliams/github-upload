# Program to convert number grades (0 -100) to letter grades (F-A)
# Author: Chris Williams

def main():
    # get number score from user
    numGrade = int(input("Enter a number grade: "))

    # Create grade scale
    grade = "F" * 60 + "D" * 10 + "C" * 10 + "B" * 10 + "A" * 10

    # get associated letter grade
    print("The score is an {}.".format(grade[numGrade]))


main()

    
