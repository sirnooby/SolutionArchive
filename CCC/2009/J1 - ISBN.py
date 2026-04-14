#Problem J1: ISBN - 2009 (SirNooby)
isbn = "9780921418"
total = 0

for i in range(3):
    isbn += input()

for i in range(len(isbn)):
    if i % 2 != 0:
        total += int(isbn[i]) * 3
    else:
        total += int(isbn[i])

print("The 1-3-sum is", total)