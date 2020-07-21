# chapter 1
# Exercise 7

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        n = 3.9 * (n - n * n)
        print(x, "      ", n)

main()
