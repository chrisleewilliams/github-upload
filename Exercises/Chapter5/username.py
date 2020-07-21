# string processing program to generate usernames
# Author: Chris Williams

def main():
    print("This program generates user names")

    first = input("Please enter your first name (all lower case):\n")
    last = input("Please enter your last name (all lower case):\n")

    uname = first[0] + last[:7]

    print("Your user name is:", uname)

main()