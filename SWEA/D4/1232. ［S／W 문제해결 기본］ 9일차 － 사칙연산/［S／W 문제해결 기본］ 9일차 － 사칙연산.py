def my_cul(num1, num2, oper):
    if oper == '-':
        return num1 - num2
    elif oper == '+':
        return num1 + num2
    elif oper == '*':
        return num1 * num2
    if oper == '/':
        return num1 // num2


def post_order(node):
    if node != 0:
        l = post_order(tree[node][0])
        r = post_order(tree[node][1])
        if tree[node][2].isnumeric():
            return int(tree[node][2])
        return my_cul(l, r, tree[node][2])


for tc in range(10):
    n = int(input())
    tree = [[0] * 3 for _ in range(n + 1)]      # [왼쪽자식, 오른쪽 자식, 저장된 값]
    for _ in range(n):
        arr = list(input().split())
        if len(arr) == 2:
            tree[int(arr[0])][2] = arr[1]
        else:
            tree[int(arr[0])][0] = int(arr[2])
            tree[int(arr[0])][1] = int(arr[3])
            tree[int(arr[0])][2] = arr[1]       # 연산자일 때 문자열로 저장
    
    print(f"#{tc + 1} {post_order(1)}")