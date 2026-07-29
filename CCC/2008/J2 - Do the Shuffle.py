#Problem J2: Do the Shuffle - 2008 (SirNooby)
playlist = "ABCDE"

while True:

    command = int(input())
    times = int(input())

    if command == 4:
        print(*playlist)
        break

    if command == 1:
        for i in range(times):
            playlist = playlist[1:] + playlist[0]
    
    if command == 2:
        for i in range(times):
            playlist = playlist[4] + playlist[:4]
    
    if command == 3:
        for i in range(times):
            playlist = playlist[1] + playlist[0] + playlist[2:]

