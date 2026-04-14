#Problem J1: The Cell Sell - 2005 (SirNooby)
daytime = int(input())
evening = int(input())
weekend = int(input())

a = round(max(0, daytime - 100) * 0.25 + evening * 0.15 + weekend * 0.20, 2)
b = round(max(0, daytime - 250) * 0.45 + evening * 0.35 + weekend * 0.25, 2)

print("Plan A costs " + f"{a:.2f}")
print("Plan B costs " + f"{b:.2f}")

if a < b:
    print("Plan A is cheapest.")
elif b < a:
    print("Plan B is cheapest.")
else:
    print("Plan A and B are the same price.")