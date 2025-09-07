students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 91),
    ("Diana", 88),
    ("Ethan", 76),
    ("Fiona", 95),
    ("George", 67),
    ("Hannah", 82),
    ("Ian", 79),
    ("Julia", 90)
]

for x in range(0 , 10):
    for y in range(x , 10):
        if(students[x][1] > students[y][1]):
            temp = students[x]
            students[x] = students[y]
            students[y] = temp

for x in range(0 , 3):
    print(f"{students[x][0]:<10}" , end='')