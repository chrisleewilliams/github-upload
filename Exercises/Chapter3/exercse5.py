# program to calculate the sell of cofee orders
# Author: Chris Williams

def main():
    print("Welcome to Konditorei's coffee shop. How many pounds of coffee would you like to purchase?")
    pounds = float(input("enter pounds here: "))
    
    coffee = 10.50
    price = coffee * pounds
    shipping = .86 * pounds + 1.50
    total = shipping + price

    print("The cost of the coffee is", round(price, 2))
    print("Shipping cost", round(shipping, 2))
    print("The total price is", round(total, 2))

main()