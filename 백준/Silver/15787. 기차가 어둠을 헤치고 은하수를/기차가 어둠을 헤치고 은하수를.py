n, m = map(int, input().split())
trains = [[0] * 20 for _ in range(n)]

for _ in range(m):
    command_list = list(map(int, input().split()))
    # 명령에 따라 분기
    if command_list[0] == 1:
        trains[command_list[1] - 1][command_list[2] - 1] = 1  
    elif command_list[0] == 2:
        trains[command_list[1] - 1][command_list[2] - 1] = 0
    elif command_list[0] == 3:
        trains[command_list[1] - 1] = [0] + trains[command_list[1] - 1][:19]
    elif command_list[0] == 4:
        trains[command_list[1] - 1] = trains[command_list[1] - 1][1:] + [0]

# 서로다른 앉은 상태 개수
visited = set()
for train in trains:
    visited.add(tuple(train))

print(len(visited))