#Problem J4 - S2: Fraction Action - 2002 (SirNooby)
import math

numerator = int(input())
denominator = int(input())

if numerator % denominator == 0:
    print(numerator // denominator)
elif numerator == 0:
    print(0)
else:
    whole = numerator // denominator
    remainder = numerator % denominator

    unreduced = denominator

    gcd = math.gcd(denominator, remainder)
    remainder //= gcd
    denominator //= gcd

    if numerator < unreduced:
        print(str(remainder) + "/" + str(denominator))
    else:
        print(str(whole) + " " + str(remainder) + "/" + str(denominator))