#Problem J4: Wait Time - 2015 (SirNooby)
messages = int(input())
times = {}
time = -1

for i in range(messages):
    action, data = input().split()

    if action == "W":
        time += (int(data) - 1)
    else:
        time += 1

    if action == "R":
        if data not in times:
            times[data] = [time, 0, True]
        else:
            times[data][0] = time
            times[data][2] = True
    
    if action == "S":
        times[data][1] += (time - times[data][0])
        times[data][2] = False
    
    
for i in sorted(times, key=int):
    if not times[i][2]:
        print(i, times[i][1])
    else:
        print(i, -1)