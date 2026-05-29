#Problem J2: 9966 - 2000 (SirNooby)
start = int(input())
end = int(input())

count = 0

numbers = ["00", "11", "69", "88", "96"]

for i in range(start, end+1):

    current = str(i)

    if len(current) > 2:
        first = 0
        last = len(current)-1
        check = True

        while first <= last:
            if current[first] + current[last] not in numbers:
                check = False
            first += 1
            last -= 1
        
        if check:
            count += 1

    else:
        if current in numbers or current == "1" or current == "8":
            count += 1

print(count)