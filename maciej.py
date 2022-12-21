'''
Zadanie domowe - wtorek
--------------------------------------------------------------------------------------------------
Napisz program, który ilustruje przykładowe metody is..., sprawdzające zawartość ciągu tekstowego.
instrukcje warunkowe mają sprawdzić czy coś zawiera tylko cyfry, tylko litery...
--------------------------------------------------------------------------------------------------
'''
jeszcze_raz = 'TAK'
while jeszcze_raz[0].lower() == 't':
    my_str = input("Wpisz dowolny ciąg znaków do sprawdzenia: ")
    if len(my_str) == 0:
        print("Nie oszukuj! 😉 Nic nie wpisałeś.")
    elif my_str.isalpha():
        print(f"Ciąg: {my_str}\njest ciągiem znakowym")
    elif my_str.isnumeric():
        print(f"Ciąg: {my_str}\njest ciągiem numerycznym")
    elif my_str.isalnum():
        print(f"Ciąg: {my_str}\njest ciągiem alfanumerycznym")
    else:
        print(f"Ciąg: {my_str}\nzawiera znaki inne niż litery i cyfry")

    jeszcze_raz = input("Czy chcesz powtórzyć? (tak/nie)")
    if len(jeszcze_raz) == 0:
        jeszcze_raz = "t"
print("Dziękuję! 😎")
