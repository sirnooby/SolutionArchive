#Problem J3: Exactly Electrical - 2017 (SirNooby)
x, y = map(int, input().split())
fx, fy = map(int, input().split())
battery = int(input())

distance = abs(fx - x) + abs(fy - y)

battery_left = battery - distance

if battery_left >= 0 and battery_left % 2 == 0:
    print("Y")
else:
    print("N")
