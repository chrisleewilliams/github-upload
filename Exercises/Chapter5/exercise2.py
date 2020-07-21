# A program to convert a numeric grade to a letter grade
# Author: CHris Williams

def main():
    intScore = int(input("Enter a quiz score 0 - 5 "))
    
    grade = ["F", "F", "D", "C", "B", "A"]

    print("The student scored an {}".format(grade[intScore]))

main()