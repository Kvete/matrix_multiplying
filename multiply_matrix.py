from random import randint


def newmas(maxim=5):
    mas = [[randint(-maxim, maxim) for j in range(2)] for j in range(2)]
    return mas


def multiply(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    k = len(arr2[0])

    c = [[None for _ in range(k)] for _ in range(m)]

    for i in range(m):
        for j in range(k):
            c[i][j] = sum(arr1[i][k] * arr2[k][j] for k in range(n))

    return c


mas1 = newmas()
for el in mas1:
    print(el)
print()
mas2 = newmas()
for el in mas2:
    print(el)
print()
for el in multiply(mas1, mas2):
    print(el)
