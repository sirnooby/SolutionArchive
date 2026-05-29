#Problem J2: Picture Perfect - 2003 (SirNooby)
while True:

    pictures = int(input())

    if pictures == 0:
        break

    smallest = 2 + pictures * 2
    
    for i in range(1, pictures+1):
        if pictures % i == 0:

            perimeter = (i * 2) + ((pictures // i) * 2)
            
            if perimeter <= smallest:
                smallest = perimeter
                dimensions = [pictures, i]
    
    print(f"Minimum perimeter is {smallest} with dimensions {dimensions[1]} x {dimensions[0]//dimensions[1]}")