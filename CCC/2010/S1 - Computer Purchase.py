#Problem S1: Computer Purchase - 2010 (SirNooby)
computers = int(input())
best = []

for i in range(computers):
    name, ram, cpu, disk = input().split()

    strength = 2 * int(ram) + 3 * int(cpu) + int(disk)

    best.append([strength, name])
    best.sort(key=lambda x: (-x[0], x[1]))
    best = best[:2]

best.sort(key=lambda x: (-x[0], x[1]))

for i in best:
    print(i[1])