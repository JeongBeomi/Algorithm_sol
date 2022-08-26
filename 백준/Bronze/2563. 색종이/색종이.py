board = [[0] * 100 for _ in range(100)]
cnt = 0
t = int(input())
for tc in range(t):
    r, c = map(int, input().split())
    for i in range(r, r + 10):
        for j in range(c, c + 10):
            if board[i][j] == 0:
                cnt += 1
                board[i][j] = 1
print(cnt)
