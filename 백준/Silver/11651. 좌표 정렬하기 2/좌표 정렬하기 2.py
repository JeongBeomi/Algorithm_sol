n = int(input())
pos_list = []
for _ in range(n):
    x, y = map(int, input().split())
    pos_list.append((x, y))
pos_list.sort(lambda x : (x[1], x[0]))

for i in pos_list:
    print(*i)