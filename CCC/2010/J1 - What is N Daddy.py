#Problem J1: What is N Daddy - 2010 (SirNooby)
n = int(input())
start = 0
count = 0

while start <= n:
    if start <= 5 and n <= 5:
        count += 1
    start += 1
    n -= 1

print(count)