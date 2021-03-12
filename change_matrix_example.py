from modBIB import show_matrix

""" Practice 5 . Algorithms for transform two-dimensional arrays """

""" Task 1
    Given two-dimensional array A integer numbers, size mxn, and given natural numbers k<m, p<n.
    Calculate sum elements of matrix, painted area including relevant(відповідними) elements row k, column p.

"""

# n, m = map(int, input().split())
# k, p = map(int, input().split())
n, m = 10, 5
k, p = 1, 9
a = [[i * m + j for j in range(n)] for i in range(m)]
print('Task 1')
show_matrix(a)
summa = 0
for row in a[:k + 1]:
    for elem in row[p - 1:]:
        summa += elem
print('Summa = ', summa)
print()

""" Task 2
    Given two-dimensional array A integer numbers, size m x n. Convert matrix, perform(виконавши) her transpose 
    ('mirror image') relatively horizontal axis.  
"""
print('Task 2')
n, m = 10, 5
a = [[i * m + j for j in range(n)] for i in range(m)]
print('Start matrix')
show_matrix(a)
print()

for i in range(m // 2):
    for j in range(n):
        a[i][j], a[m - 1 - i][j] = a[m - 1 - i][j], a[i][j]
print('Config matrix')
show_matrix(a)
print()

""" Task 3
    Given square two-dimensional array ( matrix ) A, integer numbers order n.
    Transform matrix, perform her transpose relatively side diagonal.
        
"""

print('Task 3')
n = 5
a = [[i * m + j for j in range(n)] for i in range(n)]
print('Start matrix')
show_matrix(a)
print()
for i in range(n):
    for j in range(n - i):
        a[i][j], a[n - 1 - j][n - 1 - i] = a[n - 1 - j][n - 1 - i], a[i][j]
print('Config matrix')
show_matrix(a)
print()

""" Task 4
    Given two-dimensional array A integer numbers, size n x n. Calculate sum elements painted area, 
    NO included diagonal elements.     
"""

print('Task 4')
n = 5
a = [[i * m + j for j in range(n)] for i in range(n)]
print('Start matrix')
show_matrix(a)
print()
s = 0
for i in range((n - 1)//2):
    for j in range(i + 1, n - 1 - i):
        s += a[i][j]
print('Result :')
print('Summa = ', s)
print()

""" Task 5
    Given square matrix A, size n x n, integer numbers. Transform matrix, perform 'mirror show' relatively center 
    matrix, elements 'the upper triangle' and 'the lower triangle', included with elements main and side diagonals.         
"""

print('Task 5')
n = 5
a = [[i * m + j for j in range(n)] for i in range(n)]
print('Start matrix')
show_matrix(a)
print()
for i in range(0, n//2):
    for j in range(i, n - i):
        a[i][j], a[n - 1 - i][n - 1 - j] = a[n - 1 - i][n - 1 - j], a[i][j]
print('Config matrix :')
show_matrix(a)
print()
