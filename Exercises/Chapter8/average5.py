from tkinter.filedialog import askopenfilename

def main():
    fileName = askopenfilename()
    infile = open(fileName, 'r')

    total = 0.0
    count = 0
    for line in infile:
        total = total + float(line)
        count = count + 1
        print("\nThe average of the number is", total /count)
main()