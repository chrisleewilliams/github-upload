# A program that counts the number of words in a sentence by a user
# Author: Chris Williams

def main():
    sentence = input("Enter a sentence so we can see how many words are contained inside: ")

    words = sentence.split()

    print("Your sentences has {} words in it".format(len(words)))

    input("Press <Enter> to quit")

main()

