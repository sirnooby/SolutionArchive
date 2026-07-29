#Problem J4 - S1: Trianglane - 2023 (SirNooby)
triangles = int(input())

first_row = [int(i) for i in input().split()]
second_row = [int(i) for i in input().split()]

total = 0

for i in range(triangles):
    if first_row[i] == 1:
        total += 3
        if i+1 < triangles:
            if first_row[i+1] == 1:
                total -= 1
        
        if i-1 >= 0:
            if first_row[i-1] == 1:
                total -= 1

        if i % 2 == 0 and second_row[i] == 1:
            total -= 2
        
    if second_row[i] == 1:
        total += 3
        if i+1 < triangles:
            if second_row[i+1] == 1:
                total -= 1
        
        if i-1 >= 0:
            if second_row[i-1] == 1:
                total -= 1

print(total)