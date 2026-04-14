#Problem J3: Are we there yet? - 2018 (SirNooby)
cities = list(map(int, input().split()))

for i in range(5):
    for j in range(5):
        if i > j:
            print(sum(cities[j:i]), end=" ")
        elif i == j:
            print(0, end=" ")
        else:
            print(sum(cities[i:j]), end=" ")
    print("")