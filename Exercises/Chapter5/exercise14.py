# program to count the lines words and characters in a file
# Author: Chris Williams

from tkinter.filedialog import askopenfilename, asksaveasfilename

def main():
    print("A program to count the lines, words and letters in a file.")

    print("\nSelect a file to open")
    fileName = askopenfilename()
    file = open(fileName, "r")

    
    chars = file.read()
    file.close()

    words = chars.split()

    lines = chars.split("\n")


    print("Lines: {}".format(len(lines)))
    print("Words: {}".format(len(words)))
    print("characters: {}".format(len(chars)))

    print(lines)

    

    input("Press <Enter> to quit.")

main()


