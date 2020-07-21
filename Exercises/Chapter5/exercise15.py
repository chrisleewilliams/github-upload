# A program to plota horizontal bar chart of student exam scores
# Author: Chris Williams
from tkinter.filedialog import askopenfilename, asksaveasfilename
from graphics import *

def main():
    # Student score file
    scoreFileName = askopenfilename()
    
    scoreFile = open(scoreFileName, "r")

    numOfStudents = scoreFile.readline()
    numOfStudents = int(numOfStudents)

    students = []
    for line in scoreFile.readlines():
        students.append(line)
    
    scoreFile.close() # Close student file

    
    # Create graph window
    win = GraphWin("Student Scores", 600, 600)

    # set coords of the graph window
    win.setCoords(-20, -20, 120, numOfStudents * 3)

    # List studentname, score, studentname, score ...
    studentInfo = []
    for student in students:
        studentInfo.append(student)

    win.getMouse()
    

    

main()