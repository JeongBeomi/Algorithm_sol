# append하지 않고 index로 풀기 -> append 시간 단축 가능
n, k = map(int ,input().split())
q = list(range(1, n + 1))
result = []
k -= 1
idx = k


while q:
    result.append(q.pop(idx))
    idx += k

    if len(q) == 0:
        break

    if idx >= len(q):
        idx %= len(q)

print("<" + str(result)[1:-1] + ">")