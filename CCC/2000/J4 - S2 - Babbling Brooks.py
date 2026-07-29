#Problem J4 - S2: Babbling Brooks - 2000 (SirNooby)
starting_streams = int(input())

streams = [int(input()) for i in range(starting_streams)]

while True:
    command = int(input())
    if command == 77:
        break

    if command == 88:
        stream = int(input())
        flow = streams[stream-1]
        streams[stream] += flow
        streams.pop(stream-1)

    if command == 99:
        stream = int(input())-1
        percentage = int(input())
        split_stream = streams.pop(stream)
        streams.insert(stream, round((split_stream) * ((100-percentage)/100)))
        streams.insert(stream, round(split_stream * (percentage/100)))

print(" ".join(map(str, streams)))    

