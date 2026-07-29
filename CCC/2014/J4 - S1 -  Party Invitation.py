#Problem J4 - S1: Party Invitation - 2014 (SirNooby)
people = [i for i in range(1, int(input()) + 1)]

removal_rounds = int(input())

for i in range(removal_rounds):
    multiple = int(input())
    removal = multiple-1
    for v in people:
        if 0 <= removal < len(people):
            people.pop(removal)
            removal += multiple - 1

for i in people:
    print(i)