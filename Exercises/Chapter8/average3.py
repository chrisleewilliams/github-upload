def main():
    total = 0.0
    count = 0
    x = float(input("Enter a number (Negative to quit) >> "))

    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number (Negative to quit) >> "))
    print("\nThe average of the number is", total / count)

main()
