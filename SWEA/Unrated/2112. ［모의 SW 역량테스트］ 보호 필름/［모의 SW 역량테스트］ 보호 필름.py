def dfs(r, c):
    global min_v
    if c >= min_v:      # 가지치기
        return

    if r == d:  # 모든줄의 주입여부 결정되면 성능검사
        for line in zip(*film):
            line = "".join(line)
            if line.find('0' * k) == -1 and line.find('1' * k) == -1:
                break
        else:
            min_v = c
        return

    for i in range(3):  # 투입x, A투입, B투입
        if not i:   # 투입하지않으면
            dfs(r + 1, c)
        else:       # 투입하면
            temp = film[r]                  # 복귀를 위한 임시 저장
            film[r] = [injection[i]] * w      # 주입
            dfs(r + 1, c + 1)
            film[r] = temp                  # 복귀


injection = ['0', '0', '1']   # x, A, B
t = int(input())
for tc in range(t):
    d, w, k = map(int, input().split())     # 두께, 가로, 합격기준
    film = [list(input().split()) for _ in range(d)]
    min_v = d
    dfs(0, 0)   # row, 뒤집은 횟수
    print(f"#{tc + 1} {min_v}")
