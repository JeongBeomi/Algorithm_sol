n, x = map(int, input().split())
nums = list(map(int, input().split()))
sum_num = sum(nums[:x])
sum_nums = [sum_num]

for i in range(x, n):
    sum_num -= nums[i - x]
    sum_num += nums[i]
    sum_nums.append(sum_num)

max_num = max(sum_nums)

if max_num == 0:
    print("SAD")
else:
    print(max_num)
    print(sum_nums.count(max_num))