n = int(input())
q1 = [i for i in range(1, n + 1)]
q2 = []

while True:
    if len(q1) == 1:    # 한개 남으면 탈출
        break

    v = q1.pop(0)       # 맨 위 한장 버리기
    q2.append(v)        # 출력을 위해 q2에 버린 카드 저장

    v = q1.pop(0)       # 다음 한장 맨아래로 보내기
    q1.append(v)

print(*q2, *q1)