#Problem S2: Aromatic Numbers - 2012 (SirNooby)
roman_values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

number = input()
total = 0

last_roman = 0

for i in range(len(number), 0, -2):
    segment = number[i-2:i]

    arabic = segment[0]
    roman = segment[1]

    if roman_values[roman] >= last_roman:
        total += roman_values[roman] * int(arabic)
    else:
        total -= roman_values[roman] * int(arabic)

    last_roman =  roman_values[roman]

print(total)