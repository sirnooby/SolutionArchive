#Problem S1: Baby Hop, Giant Hop - 2026 (SirNooby)
start = int(input())
end = int(input())

spaces = abs(start - end)

hop = int(input())
amount = int(input())

if spaces == 0:
    if amount == 1:
        print(0)
    else:
        print(2)
else:
    hops = spaces // hop
    left = spaces % hop

    first = min((hops + left), (hops + 1 + hop - left))
    second = min(max((hops + left), (hops + 1 + hop - left)), first+2)

    if hop == 2:
        second = first + 1
    elif first == second:
        second += 2

    if amount == 1:
        print(first)
    elif amount == 2:
        print(second)