# Program to calculate the average word length in a sentence
# Author: Chris Williams

def main():
    # get sentence from the user
    sentence = input("Enter the sentence you would like to find the average word length of: ")

    # arrange words into a list
    words = sentence.split()

    # place words into a string with no spaces
    letters = "".join(words)

    word_count = 0

    for word in words:
        word_count = word_count + 1

    print("The average lenthg of a word is {} letters.".format(len(letters) / word_count))

main()