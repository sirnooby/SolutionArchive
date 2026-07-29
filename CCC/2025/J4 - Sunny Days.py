#Problem J4: Sunny Days - 2025 (SirNooby)
days = int(input())
weather = [input() for i in range(days)]
longest = 0

j = 0
p_count = 0

for i in range(len(weather)):
    if weather[i] == "P":
        p_count += 1
    
    while p_count > 1:
        if weather[j] == "P":
            p_count -= 1
        j += 1
    
    longest = max(longest, i - j + 1)

if "P" not in weather:
    print(days - 1)
elif weather.count("P") == 1:
    print(days)
else:
    print(longest)