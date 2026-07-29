#Problem J4 - S1 - Flipper - 2019 (SirNooby)
flips = list(input())

grid = [
    [1, 2],
    [3, 4]
    ]

for i in flips:
    if i == "H":
        grid[0][0], grid[1][0] = grid[1][0], grid[0][0]
        grid[0][1], grid[1][1] = grid[1][1], grid[0][1]
    elif i == "V":
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]

print(grid[0][0], grid[0][1])
print(grid[1][0], grid[1][1])
