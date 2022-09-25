def cooking(s):
    if len(a_mat) == n // 2:    # A 재료를 두개 봅으면 B 재료는 자동 선택
        a_score = 0
        b_score = 0
        b_mat = list( nums - set(a_mat))
        for j in range(n // 2):
            for k in range(j + 1, n // 2): 
                a_score += materials[a_mat[j]][a_mat[k]]
                a_score += materials[a_mat[k]][a_mat[j]]
                b_score += materials[b_mat[j]][b_mat[k]]
                b_score += materials[b_mat[k]][b_mat[j]]
        result.append(abs(a_score - b_score))
        return

    for i in range(s, n - n // 2 + 1 + len(a_mat)): 
        a_mat.append(i)
        cooking(i + 1)
        a_mat.pop()


t = int(input())
for tc in range(t):
    n = int(input())
    materials = [list(map(int, input().split())) for _ in range(n)]
    nums = set([i for i in range(n)])
    a_mat = []
    b_mat = []
    result = []
    cooking(0)
    print(f"#{tc + 1} {min(result)}")
