t = int(input())
for tc in range(t):
    # 멈추는 정류장 카운트 리스트
    count = [0] * 1000
    for _ in range(int(input())):
        line, a, b = map(int, input().split())

        # 일반버스일 때 멈추는 정류장에 1증가
        if line == 1:
            for i in range(a, b+1):
                count[i-1] += 1
        # 급행버스일 때 멈추는 정류장에 1증가
        elif line == 2:
            for j in range(a, b+1, 2):
                count[j-1] += 1
        # 광역버스일 때 멈추는 정류장에 1증가
        else:
            if a % 2 == 0:
                for k in range(a, b+1):
                    if k % 4 == 0:
                        count[k-1] += 1
            else:
                for k in range(a, b+1):
                    if k % 3 == 0 and k % 10 != 0:
                        count[k-1] += 1

    print(f"#{tc+1} {max(count)}")