def sol(b_num, t_num):
    b_nums = set()
    for i in range(len(b_num)):
        for k in range(2):
            temp = b_num[:i] + str(k) + b_num[i + 1:]
            b_nums.add(int(temp, 2))

    for j in range(len(t_num)):
        for k in range(3):
            temp = t_num[:j] + str(k) + t_num[j + 1:]
            money = int(temp, 3)
            if money in b_nums:
                return money 

t = int(input())
for tc in range(t):
    num1 = input()
    num2 = input()
    print(f"#{tc + 1} {sol(num1, num2)}")
