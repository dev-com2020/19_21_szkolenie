slownik = {"klucz": "wartosc"}

oceny = {
    "maciek": [4, 5, 3, 4, 2],
    'pawel': [5, 5, 4, 3, 3, 1],
    'tomek': {'python': [4, 5, 3, 4],
              'java': [5, 4, 3, 2]}
}


# print(oceny['pawel'])
print(oceny['pawel'][:3])
print(oceny['tomek'])
# print(oceny['tomek']['java'])
print(oceny['tomek']['java'][:2])
print(oceny.items())
print(oceny.keys())
print(oceny.values())
print('maciek' in oceny.keys())
oceny['darek'] = 3
oceny['tomek'] = (3,)
print(oceny)