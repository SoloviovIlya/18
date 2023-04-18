n = int(input('Введите размерность списка:'))
A = list(range(1, n+1))
print(A)
x = int(input('Введите число:'))
y = x - A[0]
z = A[0]
for i in range(n):
    if x - A[i] < y and x - A[i]>=0:
        y = x - A[i]
        z = A[i]
print(z, ' - ближайшее')