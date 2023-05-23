from collections import deque

def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])

    n = len(plans)
    print(plans)
    q = deque()

    for i in range(n):
        # 마지막 plans는 다음 계획이 없다.
        if i == n - 1:
            answer.append(plans[i][0])
            while q:
                answer.append(q.pop()[0])
            break
        
        p1_h, p1_m = map(int, plans[i][1].split(":"))
        p2_h, p2_m = map(int, plans[i + 1][1].split(":"))

        plans_interval = (p2_h - p1_h) * 60 + (p2_m - p1_m)
        p1_playtime = int(plans[i][2])

        if plans_interval >= p1_playtime:
            print(i, "간격이 더길때")
            answer.append(plans[i][0])
            plans_interval -= p1_playtime
            while q and plans_interval > 0:
                print("와일문 안에서", i)
                print("와일문 안에서2", q, plans_interval)
                if q[-1][1] <= plans_interval:
                    temp = q.pop()
                    answer.append(temp[0])
                    plans_interval -= temp[1]
                else:
                    q[-1][1] -= plans_interval
                    plans_interval = 0

        else:
            print(i, "간격이 더짧을때")
            q.append([plans[i][0], p1_playtime - plans_interval])

    return answer