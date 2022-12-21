import csv

# with open('dane/osoby.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     licznik = 0
#     for row in csv_reader:
#         if licznik == 0:
#             print(f'Nazwy kolumn to {", ".join(row)}')
#             licznik += 1
#         else:
#             print(f"\t{row[0]}|\t{row[1]}|\t{row[2]}")
#             licznik += 1
#     print(f'Znalazłem {licznik} linii')


# with open('dane/osoby.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     licznik = 0
#     for row in csv_reader:
#         if licznik == 0:
#             print(f'Nazwy kolumn to {", ".join(row)}')
#             licznik += 1
#         print(f"\t{row['name']}\t|\t{row['department']}\t|\t{row['birthday month']}")
#         licznik += 1
#     print(f'Znalazłem {licznik} linii')

# with open('osoba.csv', 'w', newline="") as file:
#     writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(['imie', 'miejsce', 'miesiac'])
#     writer.writerow(['Tomasz', 'IT', 'Marzec'])

with open('osoba.csv', 'w', newline="") as file:
    names = ['imie', 'miejsce', 'miesiac']
    writer = csv.DictWriter(file, fieldnames=names)
    writer.writeheader()
    writer.writerow({'imie': 'Tomasz', 'miejsce': 'IT', 'miesiac': 'Marzec'})
