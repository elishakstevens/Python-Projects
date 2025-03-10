i = 0

while i < 15:
    i += 2
    if i == 4:
        continue
    elif i == 14:
        break
    else:
        print("{} is an even number that is smaller than 15!".format(i))
        

