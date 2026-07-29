#Problem J3 - S1: From 1987 to 2013 - 2013 (SirNooby)
year = int(input()) + 1

searching = True

while searching:
    year_list = set(list(map(int, str(year))))
    if len(year_list) == len(str(year)):
        searching = False
        print(year)
    else:
        year += 1