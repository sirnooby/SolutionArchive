#Problem S1: Good Fours and Good Fives - 2022 (SirNooby)
target = int(input())
combos = 0

for i in range((target // 4) + 1):
    
    five_value = target - (4 * i)

    if five_value % 5 == 0:
        combos += 1

print(combos)