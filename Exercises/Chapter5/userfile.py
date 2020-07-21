# program to create a file or username in batch mode
# AuthorL Chris Williams

from tkinter.filedialog import askopenfilename, askopenfilename

def main():
    print("This program creates a file of usernames from a file of names")
    

    # get the file names
    infileName = askopenfilename()
    outfileName = askopenfilename()

    # open the files
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    # process each line of the input file
    for line in infile:
        # get the first and last names from line
        first, last = line.split()
        # create username
        uname = (first[0] + last[:7]).lower()
        # write it to the output file
        print(uname, file = outfile)

    # close both files
    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)
main()

