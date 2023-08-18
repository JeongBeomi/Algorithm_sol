x, y = map(int, input().split())
win_rate = int(y * 100 / x)
# 99, 100의 승률은 변할수 없다
if win_rate >= 99:
    print(-1)
else:
    # 승률 98이하일 경우 지금까지 진행한 게임수 x 만큼 더하면 무조건 승률이 오름 
    start, end = 1, x
    # 이진 탐색
    while start < end:
        mid  = (start + end) // 2
        if int((y + mid) * 100 / (x + mid)) != win_rate:
            end = mid
        else:
            start = mid + 1

    print((start + end) // 2)
