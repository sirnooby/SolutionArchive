#Problem J3: Product Codes - 2025 (SirNooby)
codes = int(input())

for i in range(codes):
    code = input()

    current = 0
    number = 0
    partition = ""
    new_code = ""

    while current < len(code):

        character = current

        if code[character].isupper():
            new_code += code[character]
        

        if (code[character].isnumeric()):
            partition += code[character]
        else:
            if code[character] == "-" and len(partition) >= 1:
                number += int(partition)
                partition = "-"
            elif code[character] == "-" and len(partition) == 0:
                partition = "-"
            elif len(partition) >= 1:
                number += int(partition)
                partition = ""
            else:
                partition = ""
                
        current += 1
    
    if len(partition) >= 1:
        number += int(partition)

    print(new_code + str(number))

    partition = ""