def recur(start, nums):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(start, n + 1):
        nums.append(i)
        recur(i, nums)
        nums.pop()

n, m = map(int, input().split())

recur(1, [])