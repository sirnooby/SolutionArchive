#Problem S1: Surmising a Sprinters Speed - 2020 (SirNooby)
observations = int(input())
marks = []

best = 0

for i in range(observations):
    seconds, position = map(int, input().split())
    marks.append([seconds, position])

marks.sort()

for i in range(1, len(marks)):

    distance = marks[i][1] - marks[i-1][1]
    time = marks[i][0] - marks[i-1][0]

    speed = abs(distance / time)

    best = max(speed, best)

print(best)