a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(len(a))
if n == 0:
    print('array is empty')
else:
    j = 1
    k = int(input('k = '))
    while j <= k:
        b = a[n - 1]
        i = n - 2
        while i >= n // 2:
            a[i + 1] = a[i]
            i = i - 1
        a[n // 2] = b

        b = a[0]
        i = 0
        while i <= (n // 2) - 1:
            a[i] = a[i + 1]
            i = i + 1
        a[(n - 1) // 2] = b
        print((n - 1) // 2, n // 2)
        j = j + 1

print(a)
