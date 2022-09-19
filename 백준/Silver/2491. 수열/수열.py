n = int(input())
nums_list = list(map(int, input().split()))
cnt1 = 1
cnt2 = 1
result = 1
for i in range(1, n):
    if nums_list[i - 1] > nums_list[i]:
        if result < cnt1:
            result = cnt1
        cnt1 = 1
    else:
        cnt1 += 1

    if nums_list[i - 1] < nums_list[i]:
        if result < cnt2:
            result = cnt2
        cnt2 = 1
    else:
        cnt2 += 1

else:
    if result < cnt1:
        result = cnt1
    if result < cnt2:
        result = cnt2

print(result)
