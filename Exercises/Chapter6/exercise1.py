# program to print the lyrics "Old Macdonald"
# Author: Chris Williams

def eeIgh():
    print("Old Macdonald had a farm, Ee-igh, Ee-igh, Oh!")

def hada(animal):
    print(f"And on that farm he had a {animal}. Ee-igh, Ee-igh, Oh!")

def witha(noise):
    print(f"With a {noise}, {noise} here and a {noise}, {noise} there.")
    print(f"Here a {noise}, there a {noise}, every where a {noise}, {noise}.")

def verse(animal, noise):
    eeIgh()
    hada(animal)
    witha(noise)
    eeIgh()

def main():
    #animals = (("dog, bark"), ("cow", "moo"),("chicken", "cock-a-doodle"), ("cat", "meow"), ("pig","oink"))

    for x, y in (("dog", "bark"), ("cow", "moo"),("chicken", "cock-a-doodle"), ("cat", "meow"), ("pig","oink")):
        verse(x,y)
        print()

main()





    