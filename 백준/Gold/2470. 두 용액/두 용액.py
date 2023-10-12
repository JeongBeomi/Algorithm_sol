n = int(input())
liquid_list = sorted(map(int, input().split()))
answer = [0, 0]
idx1, idx2 = 0, n - 1
min_value = 2000000001

while idx1 < idx2:
    value = liquid_list[idx1] + liquid_list[idx2] 
    if abs(value) < abs(min_value):
        answer[0], answer[1] = liquid_list[idx1], liquid_list[idx2]
        min_value = value
    
    if value > 0:
        idx2 -= 1
    elif value < 0:
        idx1 += 1
    else:
        break

print(*answer)