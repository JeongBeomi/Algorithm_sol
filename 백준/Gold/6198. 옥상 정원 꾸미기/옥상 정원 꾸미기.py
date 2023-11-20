from collections import deque

s = deque()
prefix_dict = dict()
answer = 0
n = int(input())
buildings = [int(input()) for _ in range(n)]

for i in range(n - 1, -1, -1):
    h = buildings[i]
    cnt = 0
    while s and s[0][1] < h:
        cnt += 1
        # 현재 비교하는 빌딩 이전에 pop된 빌딩이 있는지 확인
        if s[0][0] in prefix_dict:
            cnt += prefix_dict[s[0][0]]
        s.popleft()
    answer += cnt

    # pop을 했다면 이후 누적합 계산을 위해 딕셔너리에 추가
    if cnt >= 1:
        prefix_dict[i] = cnt
    s.appendleft((i, h))

print(answer)
