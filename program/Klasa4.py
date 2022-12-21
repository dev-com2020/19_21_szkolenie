from abc import ABC, abstractmethod


class Ptak(ABC):

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print(f"Tu {self.gatunek}, startuje i lecę z prędkością {self.szybkosc}")

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):

    def poluj(self):
        print(f'Tu {self.gatunek},zaczynam polowanie!')
    def wydaj_odglos(self):
        print("piiii")


class Kura(Ptak):

    def __init__(self, gatunek, jaja):
        super().__init__(gatunek, 0)
        self.ilosc_jaj = jaja

    def lataj(self):
        print(f"Tu {self.gatunek},ja nie latam")
    def wydaj_odglos(self):
        print("kokokok")

    def znos_jajko(self):
        for i in range(self.ilosc_jaj):
            print("Znoszę jajko nr", i + 1)


class Mutant(Orzel, Kura, Ptak):
    def gryz(self):
        print("Atakuje!!!")
    def wydaj_odglos(self):
        print("grrrr")


orzel = Orzel('orzeł', 100)
orzel.lataj()
orzel.poluj()

kura = Kura('kura', 5)
kura.lataj()
kura.znos_jajko()

print(Mutant.mro())
