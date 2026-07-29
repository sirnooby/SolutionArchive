#Problem S2: Boxes - 2007 (SirNooby)
boxes = int(input())

volumes = []

for i in range(boxes):
    length, width, height = map(int, input().split()) 
    volumes.append([length, width, height, length * width * height])

volumes.sort(key = lambda x: (x[3]))

packages = int(input())

for i in range(packages):
    length, width, height = map(int, input().split())

    measurements = [length, width, height]

    measurements.sort()

    package = -1

    for v in range(len(volumes)):
        dimensions = sorted(volumes[v][:3])

        if dimensions[0] >= measurements[0] and dimensions[1] >= measurements[1] and dimensions[2] >= measurements[2]:
            package = v
            break

    if package == -1:
        print("Item does not fit.")
    else:
        print(volumes[package][3])