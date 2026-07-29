#Problem J1: Calendar - 2000 (SirNooby)
date, days = map(int, input().split())

print("Sun Mon Tue Wed Thr Fri Sat")

current_row = ["   "] * (date - 1)

week = date

for i in range(1, days + 1):
    current_row.append(f"{i:3d}")
    
    if week == 7 or i == days:
        print(" ".join(current_row).rstrip())
        current_row = []
        week = 0
        
    week += 1