n = int(input())
numbers = list(map(int, input().split()))
dp = [numbers[0]]

for i in range(1, n):
    dp.append(max(numbers[i], dp[i - 1] + numbers[i]))

print(max(dp))