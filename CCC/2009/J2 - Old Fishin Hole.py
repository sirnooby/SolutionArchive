#Problem J2: Old Fishin Hole - 2009 (SirNooby)
trout = int(input())
pike = int(input())
pickerel = int(input())

total = int(input())
combos = 0

for i in range((total // trout) + 1):
    for v in range((total // pike) + 1):
        for k in range((total // pickerel) + 1):
            
            value = i * trout + v * pike + k * pickerel


            if (value <= total) and (i + v + k) != 0:
                combos += 1
                print(f"{i} Brown Trout, {v} Northern Pike, {k} Yellow Pickerel")

print(f"Number of ways to catch fish: {combos}")