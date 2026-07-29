#Problem J2: Up and Down - 2010 (SirNooby)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

nikky = 0
nikky_steps = 0

byron = 0
byron_steps = 0

while True:
    if nikky_steps + a >= s:
        nikky += abs(nikky_steps - s)
        break
    else:
        nikky += a
        nikky_steps += a
    
    nikky -= b
    nikky_steps += b

while True:
    if byron_steps + c >= s:
        byron += abs(byron_steps - s)
        break
    else:
        byron += c
        byron_steps += c
    
    byron -= d
    byron_steps += d

if nikky > byron:
    print("Nikky")
elif byron > nikky:
    print("Byron")
else:
    print("Tied")