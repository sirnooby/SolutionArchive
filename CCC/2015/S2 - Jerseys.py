#Problem S2: Jerseys - 2015 (SirNooby)
jerseys = int(input())
athletes = int(input())

size_value = {"S":1, "M":2, "L":3}
sizes = [0]

count = 0

for i in range(jerseys):
    size = input()
    sizes.append(size_value[size])

for i in range(athletes):
    size, number = input().split()
    number = int(number)

    if number <= jerseys and sizes[number] != 0:
        if sizes[number] >= size_value[size]:
            count += 1
            sizes[number] = 0

print(count)