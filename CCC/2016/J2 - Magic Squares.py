#Problem J2: Magic Squares - 2016 (SirNooby)
square = []
magic = True

for i in range(4):
    line = list(map(int, list(input().split())))
    square.append(line)

magic_number = sum(square[0])

for i in square:
    row = sum(i)
    if row != magic_number:
        magic = False

for i in range(4):
    column = 0
    for v in range(4):
        column += int(square[v][i])
    if column != magic_number:
        magic = False

if magic:
    print("magic")
else:
    print("not magic")   