# avg2.py
# A simple program to average two exam scores
# illustrate use of multiple input

def main():
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter three scores seperated by a coma: "))
    average = (score1 + score2 + score3) / 3

    print("The average score is ", average)
    input("Press the <Enter> key to quit.")

main()
