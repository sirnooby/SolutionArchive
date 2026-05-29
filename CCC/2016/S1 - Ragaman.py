#Problem S1: Ragaman - 2016 (SirNooby)
word = list(input())
anagram = list(input())

leftover = []
wildcards = 0

for i in anagram:
    if i == "*":
        wildcards += 1
    else:
        if i not in word:
            leftover.append(i)
        else:
            word.remove(i)

if leftover:
    print("N")
elif len(word) == wildcards:
    print("A")