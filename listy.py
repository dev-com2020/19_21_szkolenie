# indeks = int(input('Podaj miejsce wstawienia:'))
# cyfra = input('Podaj ocenę z klasówki:')

oceny = [5, 3, 5, 3, 4, 4, 2, 1, 4, 3, 3, 4]
# print(len(oceny))
# print(oceny[:5])
print("Ilość trójek w ocenach", oceny.count(3))
print(oceny)
# oceny.insert(indeks, int(cyfra))
oceny.append(6)
oceny.remove(1)
oceny.pop()
oceny.sort()
oceny.reverse()
oceny[-1] = 3
print(oceny)
dziennik = tuple(oceny)
print(dziennik)
oceny = list(dziennik)
print(oceny)

oceny2 = oceny.copy()
oceny2[-1] = 33
print("Oceny2", oceny2)

