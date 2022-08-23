def pascal(n):
    if n > len(memo):
        add_line = [1]
        for i in range(n-2):
            add_line.append(memo[n-2][i]+memo[n-2][i+1])
        add_line.append(1)
        memo.append(add_line)
    return memo[0:n]

memo = [[1]]
t = int(input())
for tc in range(t):
    n = int(input())
    print(f"#{tc+1}")
    for k in pascal(n):
        print(*k)