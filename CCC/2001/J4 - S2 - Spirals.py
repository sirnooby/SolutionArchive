#Problem J4 - S2: Sprials - 2001 (SirNooby)
start = int(input())
end = int(input())

grid = [["" for v in range(100)] for i in range(100)]

x, y = 50, 50
grid[y][x] = str(start)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

current = start
step = 1
direction_index = 0

left_bound, right_bound = x, x
top_bound, bottom_bound = y, y

while current < end:

    for i in range(2):
        dy, dx = directions[direction_index]

        for v in range(step):
            if current >= end:
                break
            
            current += 1
            x += dx
            y += dy
            grid[y][x] = str(current)

            left_bound = min(left_bound, x)
            right_bound = max(right_bound, x)
            top_bound = min(top_bound, y)
            bottom_bound = max(bottom_bound, y)
        
        direction_index = (direction_index + 1) % 4

        if current >= end:
            break
    
    step += 1

for i in range(top_bound, bottom_bound + 1):
    row = []
    for v in range(left_bound, right_bound + 1):
        grid_value = grid[i][v]
        if grid_value == "":
            row.append("   ")
        else:
            row.append(f"{grid_value:>3}")

    print(" ".join(row))