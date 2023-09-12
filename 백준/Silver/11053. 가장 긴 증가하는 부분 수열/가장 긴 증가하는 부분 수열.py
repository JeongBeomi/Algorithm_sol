n = int(input())
nums = list(map(int, input().split()))
memo = [0] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and memo[i] < memo[j]:
            memo[i] = memo[j]
    memo[i] += 1

print(max(memo))