def hurrah():
    return("hurrah, hurrah!")

def marching(num):
    print(f"The ants go marching {num} by {num}, " + hurrah())
    print(f"The ants go marching {num} by {num}, " + hurrah())
    print(f"The ants go marching {num} by {num}, ")

def littleOne(action):
    print(f"The little one stops to {action}")

def goDown():
    print("And the all go marching down...")
    print("Into the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom1 boom!")

def verse(num, action):
    marching(num)
    littleOne(action)
    goDown()


def main():

    for x, y in (("one", "such his thumb"),("two", "tie his shoe"),("three", "climb a tree")):
        verse(x,y)
        print()
main()
