a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = int(len(a) / 2)
b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
while i <= n - 1:
    b[i] = a[n + i]
    i = i + 1

i = 0
while i <= n - 1:
    b[2 * n - 1 - i] = a[i]
    i = i + 1

i = 0
while i <= 2 * n - 1:
    a[i] = b[i]
    i = i + 1

print(a)
