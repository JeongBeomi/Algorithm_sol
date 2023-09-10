def per(n, m, nums):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            nums.append(num_list[i])
            per(n, m, nums)
            nums.pop()
            visited[i] = 0
            
n, m = map(int, input().split())
num_list = list(range(1, n + 1))
visited = [0] * n

per(n, m, [])