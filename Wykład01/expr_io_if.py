# To jest komentarz (nie wplywa na dzialanie programu).
# Kilka przykladow wyrazen (nie tylko z wykladu)

# nazwa = wyrazenie

# Proste wyrazenia arytmetyczne i logiczne:
r = 5.0
area = 3.1415 * r ** 2
# Powyzej, potegowanie (**) ma wyzszy priorytet niz *

# Czy n jest podzielne przez 7? (False)
n = 702
div7 = n % 7 == 0

# "3 < r < 6" - True; not div7 - True, zatem calosc to True
cond = 3 < r < 6 and not div7
# "a < b < c" oznacza to, co "powinno" - dwa porownania "a < b" i "b < c"

# podstawy wejscia/wyjscia
s = input("podaj napis: ")
print("podany napis:", s)

# input daje nam str (napis), ktorego nie mozemy uzyc jako liczby
# mozemy jednak uzyskac z niego liczbe (w tym przykladzie: liczbe calkowita)
r = int(input("podaj promien (liczba calkowita): "))
area = 3.1415 * r ** 2
print("pole kola: ", area)

# instrukcja warunkowa (najprostsza postac):
# if warunek:
#     (instrukcje)

n = int(input("podaj n: "))
if n < 10:
    print("n jest mniejsze od 10")
print("koniec")
