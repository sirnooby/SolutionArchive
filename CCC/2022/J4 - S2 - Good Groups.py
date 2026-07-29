#Problem J4 - S2: Good Groups - 2022 (SirNooby)
groups = int(input())
grouped = {}

for i in range(groups):
    person1, person2 = input().split()
    grouped.setdefault(person1, set()).add(person2)

ungroups = int(input())
ungrouped = {}

for i in range(ungroups):
    person1, person2 = input().split()
    ungrouped.setdefault(person1, set()).add(person2)

violations = 0
number_groups = int(input())

for i in range(number_groups):
    group = set(input().split())

    for v in group:
        if v in grouped:
            for k in grouped[v]:
                if k not in group:
                    violations += 1
    
        if v in ungrouped:
            for k in ungrouped[v]:
                if k in group:
                    violations += 1

print(violations)
