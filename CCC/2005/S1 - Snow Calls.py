#Problem S1: Snow Calls - 2005 (SirNooby)
letters = {'a': 2, 'b': 2, 'c': 2, 'd': 3, 'e': 3, 'f': 3, 'g': 4, 'h': 4, 'i': 4, 'j': 5, 'k': 5, 'l': 5, 'm': 6, 'n': 6, 'o': 6, 'p': 7, 'q': 7, 'r': 7, 's': 7, 't': 8, 'u': 8, 'v': 8, 'w': 9, 'x': 9, 'y': 9, 'z': 9}

numbers = int(input())

for i in range(numbers):
    phone_number = input()
    numerized = ""
    count = 0

    for v in phone_number:
        if v.isnumeric():
            numerized += v
            count += 1
        elif v.isalpha():
            numerized += str(letters[v.lower()])
            count += 1
        
       

        if count == 3 and len(numerized) < 8:
            numerized += "-"
            count = 0
        
        if len(numerized) > 11:
            break

    print(numerized)
    numerized = ""