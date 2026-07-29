#Problem J3: Returning Home - 2005 (SirNooby)
directions = []
last = input()

while True:
    street = input()

    if street == "SCHOOL":
        break

    direction = input()
    
    directions.append([direction, street])


for i in directions[::-1]:
    direction = i[0]
    street = i[1]

    if direction == "R":
        print(f"Turn LEFT onto {street} street.")
    elif direction == "L":
        print(f"Turn RIGHT onto {street} street.")

if last == "R":
    print(f"Turn LEFT into your HOME.")
elif last == "L":
    print(f"Turn RIGHT into your HOME.")