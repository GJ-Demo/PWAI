# Usprawnienia do własnego przemyślenia:
# - Które z liczb z range(2, n) wystarczy sprawdzić?
# - Czy nie wystarczy znaleźć tylko jeden dzielnik?
# - Jak (łatwo) obsłużyć przypadki 0 i 1 (a nawet liczby ujemne)?
# - "Upiększenie" wyjścia.


n = int(input("Wpisz n > 1: "))

found_divisor = False

for d in range(2, n):
    if n % d == 0:
        found_divisor = True

print("Liczba", n, "jest pierwsza:", not found_divisor)
