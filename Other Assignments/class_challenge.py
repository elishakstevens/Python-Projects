#Parent class
class TV_Shows:
    title = "Unknown"
    release_year = None
    seasons = None

    def __init__(self, title, release_year, seasons):
        self.title = title
        self.release_year = release_year
        self.seasons = seasons

    def info(self):
        print("\n" + self.title + " was released in " + str(self.release_year) + " and ran for " + str(self.seasons) + " seasons.")




if __name__ == "__main__":
    show1 = TV_Shows("Supernatural", 2005, 15)
    show1.info()

    show2 = TV_Shows("Buffy: The Vampire Slayer", 1997, 7)
    show2.info()
