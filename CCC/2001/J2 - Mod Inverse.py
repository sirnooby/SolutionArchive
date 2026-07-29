#Problem J2: Mod Inverse - 2001 (SirNooby)
base = int(input())
modulo = int(input())

try:
    inverse = pow(base, -1, modulo)
    print(inverse)
except:
    print("No such integer exists.")