t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    nums = input()
    secret = set()
    for _ in range(n // 4):
        for i in range(0, n, n // 4):
            secret.add(int(nums[i:i + n // 4], 16))
            # secret.add(nums[i:i + n // 4])
        nums = nums[1:n] + nums[0]
    result = sorted(list(secret), reverse=True)
    print(f'#{tc + 1} {result[k - 1]}')