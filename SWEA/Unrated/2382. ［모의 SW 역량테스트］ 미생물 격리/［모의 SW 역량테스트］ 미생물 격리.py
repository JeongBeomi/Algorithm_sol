dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)
rev = (0, 2, 1, 4, 3)

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    microbe = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(M):
        info = dict()
        for idx in range(K):
            r, c, n, d = microbe[idx]
            if not n:
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            microbe[idx][0], microbe[idx][1] = nr, nc
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                n //= 2
                d = rev[d]

            if (nr, nc) not in info.keys():
                info[(nr, nc)] = [(idx, n, d)]
            else:
                info[(nr, nc)].append((idx, n, d))

        for values in info.values():
            if len(values) == 1:
                i, n, d = values[0]
                microbe[i][2] = n
                microbe[i][3] = d
            if len(values) > 1:
                total = 0
                maxIdx, maxCnt = -1, -1
                for i, n, d in values:
                    total += n
                    if maxCnt < n:
                        maxIdx = i
                        maxCnt = n
                        
                microbe[maxIdx][2] = total
                for i, n, d in values:
                    if i != maxIdx:
                        microbe[i][2] = 0
    remains = 0
    for r, c, n, d in microbe:
        remains += n
    print("#{} {}".format(tc+1, remains))