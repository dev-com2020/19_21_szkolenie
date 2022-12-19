zbior = {1, 2, 3, 6, 7, 8}
oceny = [5, 3, 5, 3, 4, 4, 2, 1, 4, 3, 3, 4]
nowe_oceny = set(oceny)
print(nowe_oceny.intersection(zbior))
print(nowe_oceny.difference(zbior))
print(zbior.difference(nowe_oceny))
# print(nowe_oceny)
