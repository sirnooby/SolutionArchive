#Problem J5 - S2: Modern Art - 2021 (SirNooby)
rows = int(input())
columns = int(input())

paints = int(input())

total = 0

row = [0 for i in range(rows)]
column = [0 for i in range(columns)]

for i in range(paints):
    direction, number = input().split()
    number = int(number) - 1
    
    if direction == "R":
        row[number] += 1
    else:
        column[number] += 1

for i in range(rows):
    for j in range(columns):
        if (row[i] + column[j]) % 2 == 1:
            total += 1

print(total)
