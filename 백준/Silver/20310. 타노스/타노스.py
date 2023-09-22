from collections import deque 

s = deque(input())
zero_cnt = s.count("0") // 2
one_cnt = (len(s) - zero_cnt * 2) // 2
temp = deque()

while zero_cnt:
    num = s.pop()
    if num == "0":
        zero_cnt -= 1
        continue
    temp.appendleft(num)
s, temp = s + temp, deque()

while one_cnt:
    num = s.popleft()
    if num == "1":
        one_cnt -= 1
        continue
    temp.append(num)

print("".join(temp) + "".join(s))