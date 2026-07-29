#Problem J5 - S3: Floor Plan - 2003 (SirNooby)
tiles = int(input())

rows = int(input())
columns = int(input())

grid = [list(input()) for _ in range(rows)]

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

queue = []

visited = set()


def dfs(grid):
    count = 0
    while queue:

        row, column = queue.pop(-1)

        if (row, column) in visited:
            continue

        visited.add((row, column))

        count += 1
        grid[row][column] = "I"

        for i, v in directions:
            new_row, new_column = row + i, column + v
            if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] != "I":
                queue.append((new_row, new_column))

    return count

rooms = []
floored = 0


for i in range(rows):
    for v in range(columns):
        if grid[i][v] == ".":
            queue.append((i, v))
            rooms.append(dfs(grid))

rooms.sort(reverse=True)

for i in rooms:
    if tiles - i >= 0:
        tiles -= i
        floored += 1
    else:
        break

if floored != 1:
    print(str(floored) + " rooms, " + str(tiles) + " square metre(s) left over")
else:
    print(str(floored) + " room, " + str(tiles) + " square metre(s) left over")