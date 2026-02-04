#Problem J3: Icon Scaling - 2012 (SirNooby)
icon = ["*", "x", "*", " ", "x", "x", "*", " ", "*"]

scale = int(input())

for i in range(0, 9, 3):
    for j in range(scale):
        print(icon[i]*scale+icon[i+1]*scale+icon[i+2]*scale)