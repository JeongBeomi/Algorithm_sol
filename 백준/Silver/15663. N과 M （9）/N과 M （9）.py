def prm(m, arr):
    if len(arr) == m:
        result.add(tuple(arr))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            prm(m, arr + [num_list[i]])
            visited[i] = False


n, m = map(int, input().split())
num_list = list(map(int, input().split()))
result = set()
visited = [False] * n
    
prm(m, [])
for numbers in sorted(result, key = lambda x : x):
    print(*numbers)