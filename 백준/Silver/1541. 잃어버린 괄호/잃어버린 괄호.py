calculation_string = input()

# "-" 기준으로 나눈다. "-" 기준으로 나누면 그안의 요소들은 다 "+"
divide_minus = calculation_string.split("-")

# 맨처음요소 합
answer = sum(map(int, divide_minus[0].split("+")))

# 맨처음 요소 - 나머지 요소들이 최소값
for i in range(1, len(divide_minus)):
    answer -= sum(map(int, divide_minus[i].split("+")))

print(answer)