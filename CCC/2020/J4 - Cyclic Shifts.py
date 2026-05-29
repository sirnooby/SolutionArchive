#Problem J4: Cyclic Shifts - 2020 (SirNooby)
text = input()
word = input()

found = False

for i in range(len(word)):
    head = word[0]
    word = word[1:] + head

    if word in text:
        found = True

if found:
    print("yes")
else:
    print("no")