# Wybrane "punkty kratowe" na płaszczyźnie (w 1. ćwiartce)
# Powiązany temat: indeksowanie macierzy (parą współczynników)
# Przykład na zagnieżdżoną pętlę

n = 5 # na przykład

# "wszystkie" pary:
for x in range(n):
    for y in range(n):
        print(x, y)

print('-----')

# teraz tylko te, gdzie x < y:
for x in range(n):
    for y in range(n):
        if x < y:
            print(x, y)

print('-----')

# to samo, ale inaczej:
for x in range(n):
    for y in range(x + 1, n):
        print(x, y)

print('-----')

# jeszcze inaczej
for x in range(n):
    for y in range(n):
        if x >= y:
            continue # Lista 2
        print(x, y)
