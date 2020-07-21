from math import sqrt

def main():
    print("This program finds the real solutin to a quadratic.")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        discRoot = sqrt(b * b - 4 * a* c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print(f"\nThe soultions are: {root1} {root2}")
    except ValueError:
        print("\nNo real roots.")

main()