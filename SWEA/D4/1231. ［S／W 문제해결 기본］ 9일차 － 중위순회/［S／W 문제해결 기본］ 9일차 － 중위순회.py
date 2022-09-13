def inorder(n):    # 중위 순회
    if n <= N:
        inorder(2 * n)
        print(tree[n], end="")    # visit(n)
        inorder(2 * n + 1)


for tc in range(10):
    N = int(input())
    tree = [0] * 101

    for _ in range(N):      # 완저 이진트리 만들기
        input_list = list(input().split())
        tree[int(input_list[0])] = input_list[1]

    print(f"#{tc + 1}", end=" ")
    inorder(1)
    print()