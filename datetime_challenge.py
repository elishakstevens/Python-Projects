import datetime
import time
from time import strftime, localtime


def pdx():
    pdxHour = time.strftime("%H", localtime())

    return int(pdxHour)



def newYork(pdxHour):
    if pdxHour > 21:
        temp = pdxHour + 3
        nyHour = temp - 24
    else:
        nyHour = pdxHour + 3

    return nyHour

def london(pdxHour):
    if pdxHour > 16:
        temp = pdxHour + 8
        londonHour = temp - 24
    else:
        londonHour = pdxHour + 8

    return londonHour


def branchHours(pdxHour, nyHour, londonHour):
    counter = 0
    for hour in range(9, 18):        
        if pdxHour == hour:
            counter = counter + 1
        else:
            pass
    if counter == 1:
        print("Portland HQ is open.")
    else:
        print("Portland HQ is closed.")

    counter = 0
    for hour in range(9, 18):
        if nyHour == hour:
            counter = counter + 1
        else:
            pass
    if counter == 1:
        print("The New York Branch is open.")
    else:
        print("The New York Branch is closed.")

    counter = 0
    for hour in range(9, 18):
        if londonHour == hour:
            counter = counter + 1
        else:
            pass
    if counter == 1:
        print("The London Branch is open.")
    else:
        print("The London Branch is closed.")

    



if __name__ == "__main__":
    p = pdx()
    n = newYork(p)
    l = london(p)
    branchHours(p, n, l)
