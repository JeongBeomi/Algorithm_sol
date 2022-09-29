def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


v = int(input())
e = int(input())
parent = list(range(v + 1))
edge = []
for _ in range(e):
    v1, v2, w = map(int, input().split())
    edge.append((w, v1, v2))
edge.sort()
cnt = 0
cost = 0
for w, v1, v2 in edge:
    root1 = find_set(v1)
    root2 = find_set(v2)
    if root1 != root2:
        if root1 <= root2:
            parent[root2] = root1
        else:
            parent[root1] = root2
        cnt += 1
        cost += w
    if cnt == v - 1:
        break

print(cost)