#Problem J4: Snail Path - 2026 (SirNooby)
moves = int(input())
visited = set((0, 0))
current_position = [(0, 0)]
slime_spaces = 0

for i in range(moves):
    move = input()
    direction = move[0]
    spaces = int(move[1:])

    new_x, new_y = current_position.pop()
    visited.add((new_x, new_y))

    for v in range(spaces):

        if direction == "N":
            new_y -= 1
        elif direction == "S":
            new_y += 1
        elif direction == "W":
            new_x -= 1
        elif direction == "E":
            new_x += 1
        
        if (new_x, new_y) in visited:
            slime_spaces += 1
        else:
            visited.add((new_x, new_y))
    
    current_position.append((new_x, new_y))
    
print(slime_spaces)




