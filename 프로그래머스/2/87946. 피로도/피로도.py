def recur(k, dungeons, n, cnt, visited):
    if n == len(dungeons):
        return cnt
    result = 0
    for i in range(len(dungeons)):
        if not visited[i]:
            visited[i] = 1
            if k >= dungeons[i][0]:
                result = max(result, recur(k - dungeons[i][1], dungeons, n + 1, cnt + 1, visited))
            else:
                result = max(result, recur(k, dungeons, n + 1, cnt, visited))
            visited[i] = 0
    return result

def solution(k, dungeons):
    answer = -1
    visited = [0] * len(dungeons)
    answer = recur(k, dungeons, 0, 0, visited)
    return answer