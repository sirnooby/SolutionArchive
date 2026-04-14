#Problem S1: It's Cold Here! - 2000 (SirNooby)
coldest = float('inf')

while True:
    city, temperature = input().split()

    if int(temperature) < coldest:
        coldest = int(temperature)
        coldest_city = city

    if city == "Waterloo":
        print(coldest_city)
        break