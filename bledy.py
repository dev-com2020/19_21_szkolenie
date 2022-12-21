def mnozenie(a, b):
    try:
        return int(a) * int(b)
    except TypeError:
        return 0
    except ValueError:
        return "Błędnie wprowadzone dane!"


def mnozenie2(a, b):
    try:
        return int(a) * int(b)
    except (TypeError, ValueError):
        return 0


def mnozenie3(a, b):
    try:
        wynik = int(a) * int(b)
    except Exception as e:
        return f"Wystąpił błąd: {e.args}"
    else:
        return wynik
    finally:
        print(f"zmienna a: {a}, zmienna b:{b}")


print(mnozenie(3, 4))
print(mnozenie("5", "6"))
print(mnozenie("a", "b"))
print(mnozenie3("a", "b"))
print(mnozenie3(5, 6))
