# convert2.py
# A program to convert Celsius temps to Fahrenheit
# This version issues heat and cold warnings

def main ():
    celsius = float(input("what is the celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("This temperature is", fahrenheit, "degrees Fahrenheit.")

    if fahrenheit > 90:
        print("It's really hot outside. Be careful")
    elif fahrenheit < 30:
        print("Brrrr. Make sure to wrap up and stay warm.")
main()

