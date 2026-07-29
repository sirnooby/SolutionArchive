#Problem J4: Signage - 2009 (SirNooby)
width = int(input())
words = ["WELCOME", "TO", "CCC", "GOOD", "LUCK", "TODAY"]

lines = []
line_count = 0
line_words = []

for i in words:
    if line_count + len(i) + (len(line_words) - 1) >= width:
        if line_words:
            lines.append(line_words)

        line_count = 0
        line_words = []
    
    line_count += len(i)
    line_words.append(i)


if line_words:
    lines.append(line_words)


for i in lines:
    line = i

    dots = [0] * (len(line) - 1)
    letters = sum([len(i) for i in line])
    spaces = width - letters

    current = 0

    if len(line) == 1:
        print(line[0] + "." * spaces)
        continue
    else:
        while spaces > 0:
            dots[current] += 1
            current = (current + 1) % len(dots)
            spaces -= 1
    
    dots += [0]
            
    sign = ""

    for i in range(len(line)):
        sign += (line[i] + "." * dots[i])
    
    print(sign)