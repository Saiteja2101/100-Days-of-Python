class User:

    def __init__(self, hero, heroine, director):
        self.hero = hero
        self.heroine = heroine
        self.director = director

    def moviecast(self):

        # Ranveer Singh movies
        if self.hero == "ranveer singh":
            if self.heroine == "alia bhat":
                if self.director == "karan johar":
                    print("The movie name is 'Rocky Aur Rani Ki Prem Kahani'")
                elif self.director == "zoya akhtar":
                    print("The movie name is 'Gully Boy'")

            elif self.heroine == "anushka sharma":
                if self.director == "zoya akhtar":
                    print("The movie name is 'Dil Dhadakne Do'")
                elif self.director == "aditya chopra":
                    print("The movie name is 'Band Baaja Baaraat'")

        # Ranbir Kapoor movies
        elif self.hero == "ranbir kapoor":
            if self.heroine == "deepika padukone":
                if self.director == "ayan mukerji":
                    print("The movie name is 'Yeh Jawaani Hai Deewani'")
                elif self.director == "imtiaz ali":
                    print("The movie name is 'Tamasha'")

            elif self.heroine == "anushka sharma":
                if self.director == "anurag kashyap":
                    print("The movie name is 'Bombay Velvet'")
                elif self.director == "karan johar":
                    print("The movie name is 'Ae Dil Hai Mushkil'")
