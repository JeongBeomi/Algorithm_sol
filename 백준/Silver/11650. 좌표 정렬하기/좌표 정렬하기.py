n = int(input())
num_list=[]
for _ in range(n):
    n, m = map(int, input().split())
    num_list.append((n, m))
num_list.sort(lambda x: (x[0], x[1]))
for nums in num_list:
    print(*nums)