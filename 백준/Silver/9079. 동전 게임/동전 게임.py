from collections import deque

reverse_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]

def coin_game(arr):
    check_set = set()
    q = deque([(arr, 0)])
    check_set.add(int("".join(arr), 2))
    while q:
        pop_arr, n = q.popleft()
        # 십진수로 변환
        number = int("".join(pop_arr), 2)
        # 전부 뒷면 또는 전부 앞면일 경우
        if number == 0 or number == 511:
            return n
        # BFS
        for r in reverse_list:
            # 코인 뒤집기
            n_arr = reverse_coin(pop_arr, r)
            n_number = int("".join(n_arr), 2)
            # 처음 나온 조합이면 추가후 방문처리
            if n_number not in check_set:
                q.append((n_arr, n + 1))
                check_set.add(n_number)
    # 다 확인했지만 없을 경우 불가능
    return -1

def reverse_coin(coins, idx_list):
    # 얕은 복사 방지
    coin_state = coins[:]
    for idx in idx_list:
        coin_state[idx] = str((int(coin_state[idx]) + 1) % 2) 
    return coin_state

t = int(input())
test_list = []
# 입력받기 0, 1로 9개씩 t개 리스트 
for _ in range(t):
    test_list.append(["1" if c == "H" else "0" for _ in range(3) for c in input().split()])
# 각 테스트케이스별로 동전게임 진행
for i in range(t):
    print(coin_game(test_list[i]))
