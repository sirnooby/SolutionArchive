#Problem S1: Maternity - 2006 (SirNooby)
mother = input()
father = input()
babies = int(input())

genes = [0] * 5

for i in range(1, 10, 2):
    m1 = mother[i-1]
    m2 = mother[i]

    f1 = father[i-1]
    f2 = father[i]

    gene = i // 2

    if (m1.islower() and m2.islower()) and (f1.islower() and f2.islower()):
        genes[gene] = "R"
    elif (m1.isupper() and m2.isupper()) or (f1.isupper() and f2.isupper()):
        genes[gene] = "D"
    else:
        genes[gene] = "?"
        
for v in range(babies):
    baby = input()

    possible = True

    for k in range(len(baby)):
        if genes[k] == "?":
            pass
        elif baby[k].isupper() and genes[k] != "D":
            possible = False
        elif baby[k].islower() and genes[k] != "R":
            possible = False
    
    if possible:
        print("Possible baby.")
    else:
        print("Not their baby!")