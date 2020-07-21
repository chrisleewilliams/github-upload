# A program tocnvert a series of unicode numbers into a string of text
# Author: Chris Williams

def main():
    print("this program converts a sequence of Unicode numbers into", end = " ")
    print("the string of text it represents")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message: ")

    message = []

    for numStr in inString.split():
        codeNum = int(numStr)               # convert string digits to numbers                 
        message.append(chr(codeNum))        # concatenate character to message
    message =  "".join(message)

    
    print("\nThe decoded message is:", message)

    print(type(message))

main()



