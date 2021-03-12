a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(len(a))
i = 0
while i < (n - 1) // 2:
    b = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = b
    i = i + 1
    print(a)
