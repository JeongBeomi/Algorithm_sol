def sol(target, num_list):
    if len(num_list) == target:
        print(*num_list)
        return
    
    for i in range(1, n + 1):
        num_list.append(i)
        sol(target, num_list)
        num_list.pop()
        
n, m = map(int, input().split())
numbers = list(range(1, n + 1))
sol(m, [])