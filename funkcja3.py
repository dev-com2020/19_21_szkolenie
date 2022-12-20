def funkcja(x):
    return x * 2


fun = lambda x: x * 2

print(f"wynik działania funkcji {funkcja(5)}")
print(f"wynik działania funkcji {funkcja(15)}")
print(f"wynik działania funkcji {funkcja(25)}")
print(f"wynik działania funkcji {fun(30)}")
print(f"wynik działania funkcji {(lambda x: x * 2)(35)}")

wiek = lambda x: "dziecko" if x < 10 else ("Nastolatek" if x < 18 else "Dorosły")

print(wiek(5))
print(wiek(15))
print(wiek(25))
