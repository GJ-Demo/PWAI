# Dwa krótkie przykłady na niedokładność związaną z arytmetyką zmiennoprzecinkową
print(1e100 + 1 == 1e100) # True, choć matematycznie fałsz
print(((1 / 3) ** (1 / 3)) ** 3 == 1 / 3) # False, choć matematycznie prawda

# Konwersja typów
# Dokładniej: konstrukcja obiektów wybranego typu z już istniejących obiektów

n = int("20") # 20
x = float("2.5") # 2.5
n = int(10.5) # 10
s = str(100) # "100"

# Możliwe są też różne inne "sensowne" konwersje.
# Do spróbowania: int na bool i odwrotnie.

# Krotki

t = 1, "xyz", True

a, b, c = t
print(a)
print(b)
print(c)

# Krotki i napisy w pętli for:

for i in (1, 10, 100):
    print(i)

for c in "Niedź" + "wiedź": # wystarczy nawet wyrażenie, które oblicza się do napisu itp.
    print(c)
