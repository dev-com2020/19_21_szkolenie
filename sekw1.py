krotka = ()
krotka2 = (5,)
liczby = 3, 5, 7, 9
elem = 2,
imiona = 'Tomek', 'Darek', 'Adam'
imiona2 = 'Tomek', 'Darek', 'Adam', 'Paweł', "Renia"
print(krotka)
print(krotka2)
print(liczby)
print(elem)
# imie1 = imiona[0]
# imie2 = imiona[1]
# imie3 = imiona[2]
imie1, imie2, imie3 = imiona
print(imie1, imie2, imie3)

imie4, *lista, imie5, imie6 = imiona2
print(imie4, imie5, imie6)
print(lista[0])
