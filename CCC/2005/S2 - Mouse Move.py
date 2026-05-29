#Problem S2: Mouse Move - 2005 (SirNooby)
width, height = map(int, input().split())

x, y = (0, 0)

while True:
    mx, my = map(int, input().split())

    if x + mx > width:
        x = width
    elif x + mx < 0:
        x = 0
    else:
        x += mx

    if y + my > height:
        y = height
    elif y + my < 0:
        y = 0
    else:
        y += my

    if (mx, my) == (0, 0):
        break
    
    print(x, y)