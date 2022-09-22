import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))    # 작업 마감 시간으로 정렬, 동일한 마감시간 일시 먼저 시작하는 순으로 정렬
cnt = 0
t = 0               # 현재 시간
for s, e in arr:    # 스케줄표 전체 탐색
    if s >= t:      # 시작 시간이 현재 시간 보다 뒤 일때
        t = e       # 해당 스케줄 끝나는 시간으로 현재시간 이동
        cnt += 1

print(f"{cnt}")