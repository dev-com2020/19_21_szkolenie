# from program.matematyka import dodaj, odejmij, pomnoz
from program import *
from program.klasa1 import Human

# print("Witaj w moim programie!")
#
# print(matematyka.dodaj(5, 5))
# print(matematyka.odejmij(10, 5))
# print(matematyka.pomnoz(4, 2))
# print(podziel(4, 2))

czlowiek1 = Human("Adam", 25, "m")
# czlowiek1.imie = "Adam"
# czlowiek1.wiek = 25
# czlowiek1.plec = 'm'

czlowiek1.witaj()
czlowiek1.spacer()
czlowiek1.policz(5, 5)

czlowiek2 = Human("Ewa", 22, 'k')
# czlowiek2.imie = "Ewa"
# czlowiek2.wiek = 22
# czlowiek2.plec = 'k'

czlowiek2.witaj()
czlowiek2.spacer()
czlowiek2.policz(15, 65)

czlowiek3 = Human("Ala", 5, "k")
# czlowiek3.imie = "Ala"
# czlowiek3.wiek = 5
# czlowiek3.plec = 'k'

czlowiek3.witaj()
czlowiek3.spacer()
czlowiek3.policz(15, 65)
