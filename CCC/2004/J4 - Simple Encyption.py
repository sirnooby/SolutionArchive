#Problem J4: Simple Encryption - 2004 (SirNooby)
keyword = input()
old_phrase = input()
phrase = ""
encrypted = ""

for i in old_phrase:
    if i.isalpha():
        phrase += i

count = 0

for i in range(len(phrase)):
    shift = ord(keyword[count]) - 65

    current_value = ord(phrase[i]) + shift

    if current_value >= 91:
        current_value -= 26

    encrypted += chr(current_value)
    
    count += 1

    if count == len(keyword):
        count = 0

print(encrypted)