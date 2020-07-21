# futval.py
# A program to compute the value of an investment carried 10 years into the future

def main():
    print("This program calculates the future value of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    fixed_investment = eval(input("Enter the yearly invesment you will make each year: "))
    rate = eval(input("Enter the yearly rate: "))
    periods = eval(input("Enter the number of times the interest is compunded each year: "))
    investent_years = eval(input("Enter the number of years the investment will be held: "))
    apr = rate/periods
    
    for i in range(investent_years * periods):
        principal = (principal + fixed_investment) * (1 + apr) 

    print("The value in", investent_years, "years is:", principal)

main()
