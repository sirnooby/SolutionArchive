#Problem S2: Pennies in the Ring - 2008 (SirNooby)
while True:
    radius = int(input())

    pennies = 0

    if radius == 0:
        break

    pennies += (radius * 4) + 1

    for i in range(1, radius+1):
        pennies += 4 * int((radius ** 2 - i ** 2) ** 0.5)

    print(pennies)