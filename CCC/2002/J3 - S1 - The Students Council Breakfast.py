#Problem J3 - S1: The Students Council Breakfast - 2002 (SirNooby)
pink = int(input())
green = int(input())
red = int(input())
orange = int(input())

money_needed = int(input())
combos = 0
lowest = float('inf')

for i in range((money_needed // pink) + 1):
    for v in range((money_needed // green) + 1):
        for k in range((money_needed // red) + 1):
            for t in range((money_needed // orange) + 1):

                money = i * pink + v * green + k * red + t * orange

                if (money == money_needed) and (i + v + k + t) != 0:
                    combos += 1
                    lowest = min(lowest, (i+v+k+t))
                    print(f"# of PINK is {i} # of GREEN is {v} # of RED is {k} # of ORANGE is {t}")

print(f"Total combinations is {combos}.")
print(f"Minimum number of tickets to print is {lowest}.")