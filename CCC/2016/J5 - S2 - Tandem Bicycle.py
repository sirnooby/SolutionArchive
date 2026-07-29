#Problem J5 - S2: Tandem Bicycle - 2016 (SirNooby)
question = int(input())
people = int(input())
d = sorted(list(map(int, input().split())))
p = sorted(list(map(int, input().split())))

if question == 2:
    p = p[::-1]

total = 0

for i in range(people):
    total += max(d[i], p[i])

print(total)
