# plik = open('klienci.txt', 'r')
# plik = open('klienci.txt', 'w')
# plik = open('klienci.txt', 'a')

with open('klienci.txt', 'a') as plik:
    plik.write("Renia")

with open('klienci.txt', 'r') as plik:
    nowa_lista = []
    imie = plik.readline().rstrip('\n')

    while imie != "":
        nowa_lista.append(imie)
        imie = plik.readline().rstrip('\n')

# lista = ['Paweł W', 'Tomek', 'Radek']
# name = 'Paweł W'
# wiek = 35

# plik.write(name + '\n')
# plik.write(str(wiek) + '\n')
# plik.write(str(lista) + '\n')

# nowa_lista.append(plik.readline().rstrip('\n'))
# nowa_lista.append(plik.readline().rstrip('\n'))

# plik.close()
print(nowa_lista)
