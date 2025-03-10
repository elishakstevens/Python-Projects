


#Parent Class
class Twilight:
    book_series = "Twilight"
    main_character = "Bella Swan"
    rating = 4.0
    love_interst = "Edward Cullen"

    #Method for displaying some of the movie information
    def movieInfo(self):
        msg = "\nThe first installment of the {} series, Twilight, follows {} and {}.".format(self.book_series, self.main_character, self.love_interst)
        return msg

#Child Class Instance
class New_Moon(Twilight):
    rating = 4.3
    #child class attributes
    new_creature = "Werewolf"
    movie_num = 2

    #Same method as parent, with a couple of changes (polymorphism)
    def movieInfo(self):
        msg = "\nThe second installment of the {} series, New Moon, follows {} and {}.".format(self.book_series, self.main_character, self.love_interst)
        return msg

#Another child class instance
class Eclipse(Twilight):
    rating = 3.5
    #child class attributes
    plot_device = "Love Triangle"
    book_num = 3

    #Same method as parent, with a couple of changes (polymorphism)
    def movieInfo(self):
        msg = "\nThe third installment of the {} series, Eclipse, follows {} and {}.".format(self.book_series, self.main_character, self.love_interst)
        return msg





if __name__ == "__main__":

    #instantiate classes and call their methods
    book1 = Twilight()
    print(book1.movieInfo())

    book2 = New_Moon()
    print(book2.movieInfo())

    book3 = Eclipse()
    print(book3.movieInfo())
