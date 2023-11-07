a = 0

def recur(k, dungeons, n, cnt, visited):
    global a
    if n == len(dungeons):
        print(cnt)
        if a < cnt:
            a = cnt
        return
    
    for i in range(len(dungeons)):
        if not visited[i]:
            visited[i] = 1
            if k >= dungeons[i][0]:
                recur(k - dungeons[i][1], dungeons, n + 1, cnt + 1, visited)
            else:
                recur(k, dungeons, n + 1, cnt, visited)
            visited[i] = 0
    

def solution(k, dungeons):
    answer = -1
    visited = [0] * len(dungeons)
    recur(k, dungeons, 0, 0, visited)
    answer = a
    return answer