import random


class Critter(object):
    _hunger = 0
    _boredom = 0
    amount = 0

    def __init__(self, hunger, boredom):
        self.hunger = hunger
        self.boredom = boredom
        Critter.amount += 1

    @staticmethod
    def status():
        print("Całkowita liczba zwierząt na farmie wynosi: ", Critter.amount)

    @property
    def mood(self):
        c = Critter._hunger + Critter._boredom
        s = self.hunger + self.boredom
        happiness = s + c
        if happiness < 0:
            m = "Zwierz nie może być już bardziej szczęsliwy!"
        elif happiness < 50:
            m = "Zwierz jest niezbyt szczęsliwy..."
        else:
            m = "Zwierz jest nieszczęsliwy!"
        print(happiness, self.hunger, self.boredom)  # usunąć
        return m

    @classmethod
    def feed_all(cls):
        Critter._hunger -= 6
        print("Omommmommm...")

    @classmethod
    def ignore_all(cls):
        Critter._hunger += 10
        Critter._boredom += 10
        print("<Crying>")

    @classmethod
    def play_all(cls):
        Critter._boredom -= 8
        print("Wooff, woooooff!")

    def happiness(self):
        print(self.mood)


def add_animal(name):
    animals.append(name)
    name = Critter(random.randint(1, 30), random.randint(1, 30))
    name.happiness()
    print("Zwierzęta znajdujące się na farmie to: ")
    print(animals)
    Critter.status()


def main():
    global animals
    animals = []
    choice = None
    while choice != "0":
        print \
            ("""
        Farma zwierzaków

        0 - zakończ
        1 - dodaj zwierzaka
        2 - ignoruj zwierzęta
        3 - nakarm zwierzęta
        4 - pobaw się ze zwierzętami
        5 - sprawdź stan szczęścia pojedynczego zwierzaka
        """)

        choice = input("Wybierasz: ")
        print()

        # wyjdź z pętli
        if choice == "0":
            print("Do widzenia.")

        # stwórz zwierzaka
        elif choice == "1":
            name = input("Wprowadź nazwę nowego zwierzęcia: ")
            add_animal(name)
        # ignoruj zwierzęta
        elif choice == "2":
            Critter.ignore_all()

        # nakarm zwierzęta
        elif choice == "3":
            Critter.feed_all()

        # pobaw się ze zwierzętami
        elif choice == "4":
            Critter.play_all()

        # sprawdź stan szczęścia pojedynczego zwierzaka
        elif choice == "5":
            print(animals)
            name = input("Wprowadź nazwę zwierzaka z powyższej listy: ")
            name.happiness()


        # nieznany wybór
        else:
            print("\nNiestety,", choice, "nie jest prawidłowym wyborem.")


main()

input("\n\nAby zakończyć naciśnij ENTER.")