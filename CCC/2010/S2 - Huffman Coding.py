#Problem S2: Huffman Encoding - 2010 (SirNooby)
codes = int(input())
keys = {}
decoded = ""
current = 0

for i in range(codes):
    letter, binary = input().split()
    keys[binary] = letter

encoded = input()

while (current < (len(encoded) + 1)):
    if encoded[:current] in keys:
        decoded += keys[encoded[:current]]
        encoded = encoded[current:]
        current = 0
    
    current += 1

print(decoded)