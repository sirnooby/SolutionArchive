#Problem S2: TopYodeller - 2004 (SirNooby)
yodellers, rounds = map(int, input().split())

leaderboard = [[0, i+1, []] for i in range(yodellers)]

for i in range(rounds):
    round_scores = list(map(int, input().split()))

    for v in range(len(round_scores)):
        leaderboard[v][0] += round_scores[v]

    leaderboard.sort(reverse=True)

    placement = 1
    
    for k in range(len(leaderboard)):
        if k > 0 and leaderboard[k][0] != leaderboard[k-1][0]:
            placement = k + 1
        leaderboard[k][2].append(placement)
    
    leaderboard.sort(key=lambda x: (x[1]))

leaderboard.sort(key=lambda x: (-x[0], x[1]))

for i in range(len(leaderboard)):
    if leaderboard[i][0] == leaderboard[0][0]:
        print(f"Yodeller {leaderboard[i][1]} is the TopYodeller: score {leaderboard[i][0]}, worst rank {max(leaderboard[i][2])}")