#!/usr/bin/bash

# Użycie parametrów przekazanych przy wywołaniu
# Przykład: (./myscript.sh par1 par2 ...)
echo "Parametr 1: $1"
echo "Parametr 2: $2"

# Zmienne
name="Hello world!"
echo "Odczytanie zmiennej: $name"

# Prosta instrukcja warunkowa
if [ -n "$1" ]; then
    echo "Napis '$1' nie jest pusty"
fi

# Więcej klauzul
if [ -z "$2" ]; then
    echo "Parametr '$2' jest pusty"
elif [ -f "$2" ]; then
    echo "$2 istnieje i jest plikiem"
elif [ -d "$2" ]; then
    echo "$2 istnieje i jest katalogiem"
elif [ -d "$2" ]; then
    echo "$2 nie istnieje lub nie jest plikiem lub katalogiem"
fi

# Logika, np. koniunkcja
if [ -n "$2" ] && [ -f "$2" ]; then
    echo "Napis '$2' nie jest pusty i oznacza istniejący plik"
fi

# Czytanie z konsoli
read -p "Podaj liczbę: " num
echo "Podałeś $num"

# Prosta arytmetyka
((c=2*num+5))  # nie $num
echo "Wynik (2*$num+5): $c"

# Pętla po ustalonym ciągu
for i in a b c d e fgh; do
    echo $i
done

# Pętla po plikach pasujących do wzorca
for filename in /usr/bin/python3*; do
    echo $filename
done
