# A ceaser cipher to encrypt/ decrypt messages
# Author: Chris Williams

def main():
    # get key value
    key = int(input("Enter a key value: "))

    # get message to encrpyt
    message = input("Enter the message you would like to encrypt: ")

    charString = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzAB"

    encrypt = ""

    for letter in message:
        encrypt = encrypt + charString[charString.find(letter) + key]

    print("This is your encryped message: ", encrypt)

    input("Press <Enter> to decrypt your message")

    decrypt = ""
    for letter in encrypt:
        decrypt = decrypt + charString[charString.find(letter) - key]

    print("This is the decrypted message: ", decrypt)

    input("Press <Enter> to quit")

main()


