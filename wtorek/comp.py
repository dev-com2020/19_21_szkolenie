liczby = list(range(1, 11, 2))
print(liczby)

lista = [i for i in range(1, 11, 2)]
print(lista)

wyniki = ["2", "5", "53", "6", '8', '8', '6']
wyniki2 = [int(i) for i in wyniki]
print(wyniki2)

zbior = set(wyniki2)
print(zbior)
zbior2 = {i for i in wyniki2 if i >= 8}
print(zbior2)