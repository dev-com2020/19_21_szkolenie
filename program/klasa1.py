class Human:
    imie = ""
    wiek = 0
    plec = ""

    def witaj(self):
        print(f"Cześć, mam na imię {self.imie}")

    def spacer(self):
        if self.plec == 'k':
            print('Poszłam na spacer')
        else:
            print('Poszedłem na spacer')

    def policz(self):
        if self.wiek < 7:
            print('Nie potrafie jeszcze liczyć')
        else:
            print("2+2=4")
