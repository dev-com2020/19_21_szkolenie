def lista(imie="", /, *args, **kwargs):
    print(imie)
    print(args)
    print(kwargs)


lista('Tomek')
lista("Jacek", 3, imie='Tomek')
lista('Tomek', 3, 54)
