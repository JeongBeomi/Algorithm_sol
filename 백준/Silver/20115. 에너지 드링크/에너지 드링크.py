n = int(input())
drink_list = list(map(int, input().split()))
drink_list.sort(reverse = True)

# 가장많은 양에 나머지를 반씩 추가한다
total_drink = drink_list[0]
for i in range(1, n):
    total_drink += drink_list[i] / 2

print("%g" %(total_drink))