#CCO P2: Snowflakes - 2007 (SirNooby)
snowflakes_amount = int(input()) 
snowflakes = [list(map(int, input().split())) for i in range(snowflakes_amount)]

patterns = set()
found = False

def pattern_checker(snowflake):
    snowflake_patterns = []

    for i in range(6):
        new_flake = snowflake[i:] + snowflake[:i]
        snowflake_patterns.append(tuple(new_flake))
        snowflake_patterns.append(tuple(new_flake[::-1]))
    
    return min(snowflake_patterns)

for i in snowflakes:
    flake = pattern_checker(i)
    if flake in patterns:
        found = True
        break
    patterns.add(flake)


if found:
    print("Twin snowflakes found.")
else:
    print("No two snowflakes are alike.")