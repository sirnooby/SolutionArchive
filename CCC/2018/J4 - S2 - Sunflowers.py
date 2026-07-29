#Problem J4 - S2: Sunflowers - 2018 (SirNooby)
plants = int(input())

main_grid = [list(map(int, input().split())) for i in range(plants)]

def tilt(main_grid):
    new_grid = []
    for i in range(plants):
        new_grid.append([main_grid[j][i] for j in range(len(main_grid)-1, -1, -1)]) 
    return new_grid

def check():
    for t in range(len(main_grid) - 1):
        if main_grid[t][0] >= main_grid[t+1][0]:
            return False
    
    for i in range(len(main_grid)):
        current = 0
        for v in main_grid[i]:
            if v > current:
                current = v
            else:
                return False
        return True

while True:
    grid_correct = check()
    if not grid_correct:
        tilted = tilt(main_grid)
        main_grid = tilted
    else:
        for i in main_grid:
            print(*i)
        break
