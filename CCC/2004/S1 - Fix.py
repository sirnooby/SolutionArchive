#Problem S1: Fix - 2004 (SirNooby)
sets = int(input())

for i in range(sets):
    words = [input() for a in range(3)]
    check = True

    for v in words:
        if words.count(v) > 1:
            check = False
            print("No")
            break

        for x in range(1, len(v)):
            word = v[:x]
            
            if word in words and check:
                check = False
                print("No")
                break
        
        for y in range(1, len(v)):
            word_reversed = v[y:]
            
            if word_reversed in words and check:
                check = False
                print("No")
                break
        
    if check:
        print("Yes")