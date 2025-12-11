def square(x):
    y = x ** 2
    return y # "zwróć y"

a = square(50) # 2500
b = square(2) + square(3) # 2**2 + 3**2 == 13
print(f'Kwadratem {b} jest {square(b)}')


def absolute(x): # wartość bezwzględna, wbudowany odpowiednik: abs()
    if x >= 0:
        return x
    return -x # wykona się tylko wtedy, gdy x < 0

print(absolute(10))
print(absolute(-10))
# print(f"{absolute(10)=}")


def is_prime(n):
    if n < 2:
        return False
        
    for d in range(2, n):
        if n % d == 0:
            return False

    return True

n = 13
print(f"Liczba {n} jest pierwsza: {is_prime(n)}")

def a(n):
    if n == 0:
        return 0
    return 2 * a(n - 1) + 1

n = 7
print(f"Wyraz {n} ciągu: {a(n)}")
