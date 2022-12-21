import json

# with open('dane/hero.json', 'r') as f:
#     data = json.load(f)
#
# print(data)
# print(data["members"])
# print(data["members"][0])
# lista = data["members"][0]['powers']
# moc = data["members"][0]['powers'][-1]
# print(f"Ostatnia moc bohatera to {moc}")
# for i in lista:
#     print(i)

persons = {'name': 'Tomek',
           'age': 39,
           'children': None,
           'smoke': False}

# person_json = json.dumps(persons)

with open('osoba.json', 'w') as file:
    json.dump(persons, file, indent=4)

# print(person_json)
