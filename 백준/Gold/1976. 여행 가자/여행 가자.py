def find_set(node):     # 경로 압축
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


n = int(input())
m = int(input())
parent = list(range(n + 1))

for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == '1':
            root1, root2 = find_set(i + 1), find_set(j + 1)
            if root1 <= root2:      # 유니온
                parent[root2] = root1
            else:
                parent[root1] = root2

result = 'YES'
citys = list(map(int, input().split()))
temp = find_set(citys[1])
for city in citys:
    if temp != find_set(city):
        result = 'NO'

print(result)