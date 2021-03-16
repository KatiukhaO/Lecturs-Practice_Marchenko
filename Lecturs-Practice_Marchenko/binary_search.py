""" Binary search in two_dimensional arrays """

""" Task 1
    Set two-dimension array A, integer numbers, dimension m x n , elements each row whose separately orderly by 
    not-magnification , and given integer number X.
    Identify in each row separately  exist and index element, which is equal to X, algorithm binary search #1, 
    what find accidentally matching element
"""

a = [[15, 12, 10, 5],
     [5, 4, 3, 2],
     [13, 10, 5, 1]
     ]
x = 5
m = len(a)
n = len(a[0])

for i in range(m):
    L = 0
    R = n - 1
    while L <= R:
        j = (L + R) // 2
        if x == a[i][j]:
            break
        else:
            if x < a[i][j]:
                L = j + 1
            else:
                R = j - 1
    if L <= R:
        print(f'Element {x} found in row - {i + 1}, column - {j + 1} , indexs {i}, {j}')
    else:
        print(f'Element {x} not found')

""" Task 2 
    Set two-dimension array A integer numbers, dimension m x n, elements each column whose separately order by
    not-magnification and integer numbers X .
    Identify in matrix exist and index element how is equal to X, algorithm #2, what to find more left matching element.
"""

a = [[11, 2, 10, 15],
     [13, 6, 17, 15],
     [16, 15, 20, 20],
     [17, 15, 25, 36]
     ]
x = 15
n = len(a[0])
m = len(a)

for j in range(n):
    L, R = 0, m - 1
    while L < R:
        i = (L + R) // 2
        if x > a[i][j]:
            L = i + 1
        else:
            R = i
    f = True
    if x == a[R][j]:
        print(f'Element {x} found in column {j + 1} on position from index i={R}, j={j}')
        f = False
        break
if f == True:
    print(f'Element {x} not found in matrix a')

""" Task 3
    Set square matrix A, integer numbers, dimension n x n. Orderly through on row without decrease , and given 
    integer number X. 
    Identify in main diagonal exist  and index element , which is equal to X, algorithm binary search #1, what found 
    accidentally matching element. 
"""

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
x = int(input('x = '))
n = len(a)
L = 0
R = n - 1
while L <= R:
    i = (L + R) // 2
    if x == a[i][i]:
        break
    else:
        if x > a[i][i]:
            L = i + 1
        else:
            R = i - 1
if L <= R:
    print(f'Element {x} found on position with index i={i}, j={i}')
else:
    print(f'Element {x} not found in main diagonsl')