#Problem J3: Hidden Palindrome - 2016 (SirNooby)
word = input()

longest = 0

for i in range(len(word)):
    for j in range(i, len(word)+1):
        if i != j:
            if word[i:j] == word[i:j][::-1]:
                longest = max(len(word[i:j]), longest)

print(longest)