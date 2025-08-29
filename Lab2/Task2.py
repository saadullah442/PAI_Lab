totalRows = 3
totalCols = 3

a = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9],
]

b = [
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9],
]

print("Adding matrix")

for arrNum in range(totalRows):
    for index in range(totalCols):
        print(a[arrNum][index] + b[arrNum][index], end= '\t')
    print('\n')

print("Multiplication")

for arrNum in range(totalRows):
    for index in range(totalCols):
        print(a[arrNum][index] * b[arrNum][index], end= '\t')
    print('\n')
