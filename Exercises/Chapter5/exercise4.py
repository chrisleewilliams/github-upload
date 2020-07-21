# Program that allows a user to type in a phrase and output an acronym
# Author: Chris Williams

def main():
    # get phrase from user
    phrase = input("Enter a phrase you would like to get the acronym for: ")

    phrase = phrase.title()
    

    acronym = ""

    for i in phrase.split():
        acronym = acronym + i[0]

    print("the acronrm for {} is {}.".format(phrase, acronym))

main()
