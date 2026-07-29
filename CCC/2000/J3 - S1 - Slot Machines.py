#Problem J3 - S1: Slot Machines - 2000 (SirNooby)
quarters  = int(input())
slots = [int(input()) for i in range(3)]
plays = 0

while quarters > 0:
    if quarters > 0:
        quarters -= 1
        slots[0] += 1
        plays += 1

    if slots[0] == 35:
        slots[0] = 0
        quarters += 30
    
    if quarters > 0:
        quarters -= 1
        slots[1] += 1
        plays += 1

    if slots[1] == 100:
        slots[1] = 0
        quarters += 60
    
    if quarters > 0:
        quarters -= 1
        slots[2] += 1
        plays += 1
    
    if slots[2] == 10:
        slots[2] = 0
        quarters += 9

print(f"Martha plays {plays} times before going broke.")