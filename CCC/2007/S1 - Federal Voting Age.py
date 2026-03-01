#Problem S1: Federal Voting Age - 2007 (SirNooby)
dates = int(input())

for i in range(dates):
    year, month, date = map(int, input().split())

    if (2007 - year) > 18:
        print("Yes")
    elif (2007 - year) == 18:
        if (month <= 2 and date <= 27) or (month < 2):
            print("Yes")
        else:
            print("No")
    else:
        print("No")