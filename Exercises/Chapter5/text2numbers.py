# A program to convert a textual message into a sequence of numbers
# utilizing the underlying unicode encoding

def main():
    print("This program converts a textual message into a sequence of",end = " ")
    print("numbers utilizing the underlying Unicode encoding")

    # get the message to encode
    message = input("please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end = " ")

    print()
main()