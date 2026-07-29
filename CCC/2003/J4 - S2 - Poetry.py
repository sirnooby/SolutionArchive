#Problem J4 - S2: Poetry - 2003 (SirNooby)
poems = int(input())
vowels = "aeiou"

for i in range(poems):

    rhymes = []

    for v in range(4):
        line = input().split()[-1].lower()

        vowel_found = False

        for k in range(len(line)-1, -1, -1):
            if line[k] in vowels:
                rhymes.append(line[k:])
                vowel_found = True
                break
        
        if not vowel_found:
            rhymes.append(line)


    if rhymes[0] == rhymes[1] == rhymes[2] == rhymes[3]:
        print("perfect")
    elif rhymes[0] == rhymes[1] and rhymes[2] == rhymes[3]:
        print("even")
    elif rhymes[0] == rhymes[2] and rhymes[1] == rhymes[3]:
        print("cross")
    elif rhymes[0] == rhymes[3] and rhymes[1] == rhymes[2]:
        print("shell")
    else:
        print("free")