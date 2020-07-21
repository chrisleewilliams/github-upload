# convert.py
# A program to convert celsius temps to fahrenheit
# by Chris

def main():
    print("Enter a temperature in celsius so that I may convert the temperature to fahrenheit.")
    print("celsius | Fahrenheit")
    print("-" * 30)
    for i in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        fahrenheit = 9/5 * i + 32
        print(i, "     |     ", fahrenheit, )
    input("Press the <Enter> key to quit.")

main()
