n, m = map(int, input().split())
num_list = list(map(int, input().split()))
print(sorted(num_list, reverse=True)[m-1])