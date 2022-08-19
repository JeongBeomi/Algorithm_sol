t = int(input())
for tc in range(t):
    n = int(input())
    card_list = list((input().split()))
    card1 = card_list[0:len(card_list) // 2 + len(card_list) % 2]
    card2 = card_list[len(card_list) // 2 + len(card_list) % 2:]

    print(f"#{tc+1}", end=" ")
    for i in range(n):
        if i % 2 == 0:
            print(card1[i // 2], end=" ")
        if i % 2 == 1:
            print(card2[i // 2], end=" ")
    print()