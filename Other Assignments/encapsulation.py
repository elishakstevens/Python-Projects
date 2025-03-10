
#Protected attribute - one underscore
class secretNum:
    def __init__(self):
        self._number = 0


#Private attribute - double underscore
class secretLett:
    def __init__(self):
        self.__letter = "b"

    def getLetter(self):
        print(self.__letter)

    def setLetter(self, letter):
        self.__letter = letter


#Object making use of protected attribute
obj1 = secretNum()
obj1._number = 8
print(obj1._number)

#Object making use of private attribute
obj2 = secretLett()
obj2.getLetter()
obj2.setLetter("g")
obj2.getLetter()

    
