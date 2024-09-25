
def myFunction(name, color):
    mySentence = "{} is {}'s favorite color!".format(color, name)
    print(mySentence)

def getName():
    go = True
    while go:
        name = input("What's your name? ")
        if name == "":
            print("Please provide your name.")
        else:
            go = False
    return name
    
def getColor():
    go = True
    while go:
        color = input("What's your favorite color? ")
        if color == "":
            print("Please provide your favorite color.")
        else:
            go = False
    return color

myFunction(getName(), getColor())


