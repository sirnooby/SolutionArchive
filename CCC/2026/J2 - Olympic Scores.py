#Problem J2: Olympic Scores - 2026 (SirNooby)
scores = [int(input()) for i in range(5)]
difficulty = int(input())

scores.remove(min(scores))
scores.remove(max(scores))

print(sum(scores) * difficulty)