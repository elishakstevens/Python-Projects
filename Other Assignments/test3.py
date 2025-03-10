

def getInfo():
    fname = input("\nWhat is your first name? ")
    lname = input("\nWhat is your last name? ")
    return fname, lname

def message():
    go = True
    while go:
        fname, lname = getInfo()
        try:
            fullName = fname + ' ' + lname
            go = False
        except:
            print("\nOops, you provided invalid input. The program will close now.")
    print("\nWelcome to Python {}!".format(fullName))





if __name__ == "__main__":
   message()
