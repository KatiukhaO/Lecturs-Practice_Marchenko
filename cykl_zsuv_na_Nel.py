a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(len(a))
b = 0
j = 1
k = 3
while j <= k:
    b = a[n - 1]
    i = n - 2
    while i >= 0:
        a[i + 1] = a[i]
        i = i - 1
    j = j + 1
    a[0] = b

    print(a)
