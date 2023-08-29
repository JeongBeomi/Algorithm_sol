n = int(input())
stairs = [0] * (n + 1)
for i in range(1, n + 1):
    stairs[i] = int(input())
if n <= 2:
    print(sum(stairs))
else:    
    memo = [0, stairs[1], stairs[1] + stairs[2]]
    while len(memo) <= n:
        memo.append(max(memo[-2], memo[-3] + stairs[len(memo) - 1]) + stairs[len(memo)])

    print(memo[n]) 