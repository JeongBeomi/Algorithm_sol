n = int(input())
# [[자식 노드들], 부모노드]
tree = [[[], -2] for _ in range(n)]
parents =list(map(int, input().split()))
for i in range(len(parents)):
    # 부모노드 저장
    tree[i][1] = parents[i]
    # -1 이면 루트 노드라서 자식노드 따로 추가할 필요 없음
    if parents[i] == -1:
        continue
    # 자식노드 저장
    tree[parents[i]][0].append(i)

remove_node = int(input())
# 맨처음 지우는 노드를 부모노드의 자식노드 리스트에서 삭제처리
if remove_node in tree[tree[remove_node][1]][0]:
    tree[tree[remove_node][1]][0].remove(remove_node)
# 노드를 따라가면서 삭제처리
remove_nodes = [remove_node]
while remove_nodes:
    remove_n = remove_nodes.pop()
    remove_nodes += tree[remove_n][0]
    tree[remove_n] = [[], -2]
answer = 0
# 살아있는 리프노드 수 확인
for node in tree:
    if node[1] != -2 and not node[0]:
        answer += 1

print(answer)