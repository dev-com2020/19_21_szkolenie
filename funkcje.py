def drukuj_napis():
    print("NAPIS")


def drukarka(tekst, ile_razy):
    wydruk = (tekst + " ") * ile_razy
    return wydruk


def drukarka2(tekst, ile_razy):
    return (tekst + " ") * ile_razy


def drukarka3(tekst, ile_razy=1):
    return (tekst + " ") * ile_razy


lista = [drukarka("NAPIS", 5), drukarka2("NAPIS", 2), drukarka3(ile_razy=5, tekst="5"), "tomek"]
print(lista)
