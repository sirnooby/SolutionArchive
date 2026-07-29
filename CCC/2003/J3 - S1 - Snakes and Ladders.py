#Problem J3 - S1: Snakes and Ladders - 2003 (SirNooby)
square = 1

snakes = {54:19,90:48,99:77}

ladders = {9:34,40:64,67:86}

while True:
    roll = int(input())

    if roll == 0:
        print("You Quit!")
        break

    if 100 >= roll + square:
        square += roll

        if square in ladders:
            square = ladders[square]
        
        if square in snakes:
            square = snakes[square]
            
    print("You are now on square", square)

    if square == 100:
        print("You Win!")
        break