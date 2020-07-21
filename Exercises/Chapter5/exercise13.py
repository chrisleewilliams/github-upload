# A batch version of of the improved futval program created in chapter 5
# Author: Chris Williams
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def main():
    print("This program calculates the future value of a 10-year investment.\n")

    inputFileName = askopenfilename()
    outputFileName = asksaveasfilename()
    
    inputFile = open(inputFileName, "r+")
    outputFile = open(outputFileName, "r+")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years you will hold the investment: "))

    print(principal, apr, years, file=inputFile)

    
    inputFile.flush()
    os.fsync()
    

    data = inputFile.readline()
    fprincipal , fapr, fyears = data.split()
        
    fprincipal = float(fprincipal)
    fapr = float(fapr)
    fyears = int(fyears)


    print("{:9} {:9}".format("Year","Value"), file=outputFile)
    print("-" * 30, file=outputFile)

    for i in range(fyears):
        fprincipal = fprincipal * (1 + fapr)
        print("{:<9} ${:<9.2f}".format(i + 1, fprincipal), file=outputFile)

    
    outputFile.close()
    inputFile.close()

    input("Press <Enter> to quit")
main()