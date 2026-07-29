#Problem S1: Cool Numbers  - 2009 (SirNooby)
start = int(input())
end = int(input())

count = 0

for i in range(end):
    cool = (i ** 6)
    if start <= cool <= end:
        count += 1
    elif cool > end:
        break
    
print(count)