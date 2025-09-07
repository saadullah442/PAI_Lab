pairs = [
    (3, 7),
    (10, 25),
    (14, 18),
    (22, 5),
    (9, 33),
    (42, 17),
    (28, 36),
    (11, 19),
    (7, 21),
    (15, 29)
]
lowestSum = 9999;
for x in pairs:
    if( x[0] + x[1] < lowestSum):
        lowestSum = x[0] + x[1]
    
print(f"{lowestSum =:>3}")