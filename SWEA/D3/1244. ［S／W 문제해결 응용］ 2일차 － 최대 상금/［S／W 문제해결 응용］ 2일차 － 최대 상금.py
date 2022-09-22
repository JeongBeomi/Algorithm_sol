def search(i):
    global max_v
    if i == n:      # 교환 횟수만큼 교환했을 때, 가장 큰 값
        value = max(repeated[i - 1])
        if max_v < value:
            max_v = value
    else:
        for j in range(length - 1):
            for k in range(j + 1, length):
                board[j], board[k] = board[k], board[j]
                temp = int("".join(board))
                if temp not in set(repeated[i]):    # 중복 가지치기
                    repeated[i].append(temp)
                    search(i + 1)
                board[j], board[k] = board[k], board[j]     # 재귀 탈출시 배열 복귀


t = int(input())
for tc in range(t):
    board, n = input().split()
    n = int(n)
    board = list(board)
    repeated = [[] for _ in range(n)]
    length = len(board)
    max_v = 0
    search(0)
    print(f"#{tc + 1} {max_v}")
