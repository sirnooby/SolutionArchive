#Problem J4: Arrival Time - 2016 (SirNooby)
hour, minute = map(int, input().split(":"))

distance = 120

while distance > 0:

    if 7 <= hour < 10 or 15 <= hour < 19:
        distance -= 0.5
    else:
        distance -= 1

    minute += 1
    if minute == 60:
        minute = 0
        hour = (hour + 1) % 24

print(f"{hour:02d}:{minute:02d}")