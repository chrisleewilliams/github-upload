# Program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number of hydrogen, carbon and oxygen atoms in a molecule
# Author: Chris Williams

def main ():
    print("Hello! If you enter in the number of hydrogen, carbon and oxygen atoms in the molecule I will calculate the molecular weight(In grams per mole) of a carbohydrate.")
    h = int(input("Please enter the number of hydrogen molecules: "))
    c = int(input("Now enter the carbon molecules: "))
    o = int(input("And last the oxygen molecules: ")) 

    hydrogen = h * 1.000794
    carbon = c * 12.0107
    oxygen = o * 15.9994

    total_weight = hydrogen + carbon + oxygen

    print("The total weight is ", total_weight)

main()


    