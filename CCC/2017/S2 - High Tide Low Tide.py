#Problem S2: High Tide, Low Tide - 2017 (SirNooby)
tides = int(input())
measurements = sorted(list(map(int, input().split())))

middle = int(-(-(tides / 2) // 1))

low = sorted(measurements[:middle])
high = sorted(measurements[middle:], reverse=True)

while True:
    if len(low) > 0:
        value = low.pop()
        print(value, end=" ")
    
    if len(high) > 0:
        value = high.pop()
        print(value, end=" ")
    
    if len(low) == 0 and len(high) == 0:
        break