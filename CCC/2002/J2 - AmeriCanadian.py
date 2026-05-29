#Problem J2: AmeriCanadian - 2002 (SirNooby)
vowels = ["a", "e", "i", "o", "u", "y"]
while True:
    word = input()

    if word == "quit!":
        break

    if len(word) > 4:
        ending = word[len(word)-2:]

        if ending == "or" and word[len(word)-3] not in vowels:
            print(word[:len(word)-2] + "our")
        else:
            print(word)
    else:
        print(word)