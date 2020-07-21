# A program to calculate the value of some change in dollars
# This version represents the total cash in cents

def main():
    print("Change Counter\n")
    print("please enter the count of each coin type.")

    quarters = int(input("Quarters"))
    dimes = int(input("dimes"))
    nickels = int(input("nickels"))
    pennies = int(input("pennies"))

    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print("the total value of your change is ${}.{:0>2}".format(total // 100, total % 100))

main()