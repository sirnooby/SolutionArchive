#Problem J3: Rovarspraket - 2015 (SirNooby)
word = input()

vowels = "aeiou"
alphabet = "abcdefghijklmnopqrstuvwxyz"
encoded = ""

for i in word:
    encoded += i
    if i not in vowels:
        
        letter = alphabet.find(i)
        closest = []
        moves = 1

        while True:
            forward = (letter + moves)
            backward = (letter - moves)

            if backward <= 25 and alphabet[backward] in vowels:
                closest.append(alphabet[backward])
                break

            if forward <= 25 and alphabet[forward] in vowels:
                closest.append(alphabet[forward])
                break
            
            moves += 1

        encoded += closest[0]

        for i in range(1, 3):
            shift = alphabet[min(letter+i, 25)]

            if shift not in vowels:
                encoded += alphabet[min(letter+i, 25)]
                break
            
print(encoded)