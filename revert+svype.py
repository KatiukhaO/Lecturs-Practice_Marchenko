a=[1,2,3,4,5,6,7,8,9,10]
n=int(len(a)/2)
i = 0
while i <= n-1:
    b = a[i]
    a[i] = a[2*n - 1 - i]
    a[2*n - 1 - i] = b
    i = i + 1  

i = 0 
while i <= n//2 - 1:
    b = a[i]
    a[i] = a[n - 1 - i]
    a[n-1-i] = b
    i = i + 1 
print(a)
