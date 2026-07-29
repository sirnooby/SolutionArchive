#Problem J4: Favourite Times - 2017 (SirNooby)
end = int(input())

time = ["12", "00"]
count = 0

if end >= 720:
    count += (int(end / 720) * 31)
    end -= (int(end / 720) * 720)

while end > 0:

    hour = time[0]
    minutes = time[1]

    if minutes == "59":
        if hour == "12":
            time[0] = "1"
        else:
            time[0] = str(int(time[0]) + 1)
        time[1] = "00"
    elif int(minutes) < 9:
        time[1] = "0" + str(int(time[1]) + 1)
    else:
        time[1] = str(int(time[1]) + 1)

    
    digits = time[0] + time[1]
    sequence = []
    
    for i in range(len(digits)):
        if i > 0:
            sequence.append(int(digits[i]) - int(digits[i-1]))

    is_sequence = True
    
    for i in sequence:
        if i != sequence[0]:
            is_sequence = False
    
    if is_sequence:
        count += 1
            
    end -= 1

print(count)