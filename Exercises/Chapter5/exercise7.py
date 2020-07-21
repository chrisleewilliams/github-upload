# A program to create a Ceasar cipher using a fixed number as a key value
# Author: Chris Williams

def main():
    # get the message to encrpt from the user
    message = input("Enter the message to encrpyt: ")

    key = 2    # key value

    encrypt = ""

    # Encrypt the message
    for letter in message:
        encrypt = encrypt + chr(ord(letter) + key)

    print("the encrypted message is: " + encrypt)

    input("\nTo decrypt the message press <Enter>.")

    # Decrypt the message
    decrypt = ""
    for letter in encrypt:
        decrypt = decrypt + chr(ord(letter) - key)

    print("The decrypted messae is: " + decrypt)

    input("Press <Enter> to quit the program")


main()
    