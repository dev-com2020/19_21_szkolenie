# class Human:
#     imie = ""
#     wiek = 0
#     plec = ""
#
#     def witaj(self):
#         print(f"Cześć, mam na imię {self.imie}")
#
#     def spacer(self):
#         if self.plec == 'k':
#             print('Poszłam na spacer')
#         else:
#             print('Poszedłem na spacer')
#
#     def policz(self, a, b):
#         if self.wiek < 7:
#             print('Nie potrafie jeszcze liczyć')
#         else:
#             print("Wynik dodawania =", a + b)
#

class Human:
    '''
    Klasa Human symuluje powstawanie czlowieka
    '''

    def __init__(self, imie="Alicja", wiek=0, plec='k'):
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def witaj(self):
        '''
        Metoda witaj symuluje powitanie
        :return: komunikat z imieniem
        '''
        print(f"Cześć, mam na imię {self.imie}")

    def spacer(self):
        if self.plec == 'k':
            print('Poszłam na spacer')
        else:
            print('Poszedłem na spacer')

    def policz(self, a, b):
        if self.wiek < 7:
            print('Nie potrafie jeszcze liczyć')
        else:
            print("Wynik dodawania =", a + b)
