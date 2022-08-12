en_num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
t = int(input())
for tc in range(t):
    n, x = input().split()
    str_num_list = input()
    print(n)
    for en_num in en_num_list:
        print(f"{en_num} " * str_num_list.count(en_num))