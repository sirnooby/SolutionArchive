#Problem S2: Pretty Average Primes - 2019 (SirNooby)
cases = int(input())

limit = 2000000

primes = [True] * (limit + 1)
current = 2

while current ** 2 <= limit:
    if primes[current]:
        for i in range(current ** 2, limit + 1, current):
            primes[i] = False
    current += 1

for i in range(cases):
    target = int(input())

    for v in range(2, (target * 2) + 1):
        target_sum = (target * 2) - v

        if primes[v] and primes[target_sum]:
            print(v, target_sum)
            break