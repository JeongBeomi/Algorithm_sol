# s, e 조합을 위한 시작과 끝 인덱스 / cnt, taget_cnt 선택한 치킨집 수 / store_list bfs시 사용할 시작점 리스트
def select_store(s, e, cnt, target_cnt, store_list):
    global min_distance
    # 치킨집을 다 선택하면 거리 측정
    if cnt == target_cnt:
        measure(store_list)
        
    for i in range(s, e):
        # 치킨집 추가
        store_list.append(chicken_stores[i])
        select_store(i + 1, e, cnt + 1, target_cnt, store_list)
        # 제거
        store_list.pop()
        
def measure(stores):
    global min_distance
    h_cnt = len(houses)
    distances = [n * n] * h_cnt
    # 해당집에서 가장 가까운 가게와의 거리를 구한다
    for idx in range(h_cnt):
        for store in stores:
            distances[idx] = min(distances[idx], abs(houses[idx][0] - store[0]) + abs(houses[idx][1] - store[1]))
    sum_distance = sum(distances)
    min_distance = min(min_distance, sum_distance)
    

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken_stores = []
houses = []
min_distance = n * n * n * n

# 치킨집, 집 위치 찾기
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken_stores.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))
            

stores_cnt = len(chicken_stores)
select_store(0, stores_cnt, 0, m, [])

print(min_distance)