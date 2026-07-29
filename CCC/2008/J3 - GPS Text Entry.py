#Problem J3: GPS Text Entry - 2008 (SirNooby)
keyboard = [
    ["A","B","C","D","E","F"],
    ["G","H","I","J","K","L"],
    ["M","N","O","P","Q","R"],
    ["S","T","U","V","W","X"],
    ["Y","Z"," ","-",".","*"]]

word = input() + "*"
keystrokes = 0
position = [0, 0]

for i in word:
    for v in range(len(keyboard)):

        try:
            x = abs(position[0] - keyboard[v].index(i))
            y = abs(position[1] - v)

            position = [keyboard[v].index(i), v]

            keystrokes += (x + y)

        except:
            pass

print(keystrokes)
