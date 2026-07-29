#Problem S2: Attack of the CipherTexts - 2006 (SirNooby)
letters = {
    "A": ".",
    "B": ".",
    "C": ".",
    "D": ".",
    "E": ".",
    "F": ".",
    "G": ".",
    "H": ".",
    "I": ".",
    "J": ".",
    "K": ".",
    "L": ".",
    "M": ".",
    "N": ".",
    "O": ".",
    "P": ".",
    "Q": ".",
    "R": ".",
    "S": ".",
    "T": ".",
    "U": ".",
    "V": ".",
    "W": ".",
    "X": ".",
    "Y": ".",
    "Z": ".",
    " ": ".",
}

alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "
]


plaintext = list(input())
cipher = list(input())

ciphertext = list(input())

for i in range(len(plaintext)):
    letters[cipher[i]] = plaintext[i]

message = ""

missing = []

for i in letters:
    if letters[i] == ".":
        missing.append(i)

    if letters[i] in alphabet:
        alphabet.remove(letters[i])

for i in ciphertext:
    if len(missing) == 1 and i == missing[0]:
        if len(alphabet) == 1:
            message += alphabet[0]
    else:
        message += letters[i]

print(message)