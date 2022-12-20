# znaPythona = 0
#
# if znaPythona:
#     print("Gratulacje!")
# else:
#     print("Musisz się nauczyć!")
#
# print("...Kolejne instrukcje programu...")

# znaPythona = input("Czy znasz język?(Wprowadź 't' lub 'n')")
#
# if znaPythona == 'tak' or znaPythona == 'Tak' or znaPythona == 't':
#     print("Gratulacje!")
# elif znaPythona == 'nie':
#     print("Musisz się nauczyć!")
# else:
#     print("Nie ma takiego wyboru!")
#
# print("...Kolejne instrukcje programu...")

# podatek = 9999
# if 500 <= podatek <= 1000:
#     oplata = 0.0
# elif podatek < 3000:
#     oplata = 0.2
# elif podatek < 5000:
#     oplata = 0.35
# elif podatek != 9999:
#     oplata = -0.2
# else:
#     oplata = 0.45
#
# print(oplata)

# zamowienie = 247

# if zamowienie > 100:
#     rabat = 0.10
# else:
#     rabat = 0.0
#
# print(f"Twoje zamówienie na kwotę {zamowienie} otrzymuje rabat w wysokości: {rabat}")

# rabat = 0.10 if zamowienie > 100 else 0.0
# print(f"Twoje zamówienie na kwotę {zamowienie} otrzymuje rabat w wysokości: {rabat}")

alert = 'console'
error = 'medium'
message = 'warning!!!'

if alert == 'console':
    print(message)
elif alert == 'email':
    if error == 'critical':
        print("Wysyłam maila....")
    elif error == 'medium':
        print("Wysyłam mniej ważnego maila....")
    else:
        print("Wysyłam maila ale później")
else:
    print("Błędny status alertu")