#Problem J3: Good Times - 2009 (SirNooby)
time = int(input())

print(f"{time} in Ottawa")
print(f"{(time - 300) % 2400} in Victoria")
print(f"{(time - 200) % 2400} in Edmonton")
print(f"{(time - 100) % 2400} in Winnipeg")
print(f"{time} in Toronto")
print(f"{(time + 100) % 2400} in Halifax")

johns = (time + 130) % 2400
if johns % 100 >= 60:
    johns = johns + 40
    
print(f"{johns % 2400} in St. John's")