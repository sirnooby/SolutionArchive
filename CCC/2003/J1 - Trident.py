#Problem J1: Trident - 2003 (SirNooby)
height = int(input())
spacing = int(input())
handle = int(input())

middle = spacing * 2 + 3

for i in range(height):
    print("*" + " "*spacing + "*" + " "*spacing + "*")

print("*"*middle)

for i in range(handle):
    print(" "*(spacing+1) + "*")