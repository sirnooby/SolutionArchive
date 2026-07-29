#Problem J5 - S2: Assigning Partners - 2014 (SirNooby)
groups = int(input())

group1 = input().split(" ")
group2 = input().split(" ")

partners = []

for i in range(groups):
    partners.append(sorted(group1[i]+group2[i]))
        
for i in range(len(partners)):
    if partners.count(partners[i]) == 1:
        print("bad")
        break
    elif i == len(partners)-1:
        print("good")