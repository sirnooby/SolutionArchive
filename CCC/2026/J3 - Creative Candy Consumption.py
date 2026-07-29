#Problem J3: Creative Candy Consumption - 2026 (SirNooby)
ngoc = list(input())
minh = list(input())
    
ngoc_eaten = 0
minh_eaten = 0

candy_table = {'R': 'G', 'G': 'B', 'B': 'R'}

n = 0
m = 0

while n < len(ngoc) and m < len(minh):
    candy1 = ngoc[n]
    candy2 = minh[m]

    if candy1 == candy2:
        ngoc_eaten += 1
        minh_eaten += 1
        n += 1
        m += 1
    elif candy_table[candy1] == candy2:
        ngoc_eaten += 1
        m += 1
    else:
        minh_eaten += 1
        n += 1

ngoc_eaten += (len(ngoc) - n)
minh_eaten += (len(minh) - m)    

print(ngoc_eaten)
print(minh_eaten)