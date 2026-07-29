#Problem J3: Punchy - 2010 (SirNooby)

variables = {
    "A":0,
    "B":0
}

while True:
    instructions = input().split()

    if instructions[0] == "1":
        variables[instructions[1]] = int(instructions[2])
    
    if instructions[0] == "2":
        print(variables[instructions[1]])
    
    if instructions[0] == "3":
        variables[instructions[1]] = variables[instructions[1]] + variables[instructions[2]]
    
    if instructions[0] == "4":
        variables[instructions[1]] = variables[instructions[1]] * variables[instructions[2]]

    if instructions[0] == "5":
        variables[instructions[1]] = variables[instructions[1]] - variables[instructions[2]]

    if instructions[0] == "6":
        variables[instructions[1]] = int(variables[instructions[1]] / variables[instructions[2]])

    if instructions[0] == "7":
        break