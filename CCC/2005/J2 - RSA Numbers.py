#Problem J2: RSA Numbers - 2005 (SirNooby)
start_number = int(input())
end_number = int(input())

rsa_numbers = 0

for i in range(start_number, end_number+1):
    divisors = 0
    for v in range(1, i+1):
        if i % v == 0:
            divisors += 1

    if divisors == 4:
        rsa_numbers += 1
    
print("The number of RSA numbers between", start_number, "and", end_number, "is", rsa_numbers)
