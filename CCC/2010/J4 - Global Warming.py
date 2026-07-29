#Problem J4: Global Warming - 2010 (SirNooby)
while True:
    data = list(map(int, input().split()))

    if data[0] == 0:
        break
    
    values = data[1:]
    sequence = []
    current = 1

    if len(values) == 1:
        print("0")

    while current < len(values):
        sequence.append(values[current] - values[current - 1])
        current += 1

    for i in range(1, len(sequence) + 1):
        pattern = sequence[:i]

        repeat = (pattern * (len(sequence) // i + 1))[:len(sequence)]

        if repeat == sequence:
            print(i)
            break