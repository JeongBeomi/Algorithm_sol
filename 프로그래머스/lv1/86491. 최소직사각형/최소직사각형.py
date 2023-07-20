def solution(sizes):
    wallet_x, wallet_y = 0, 0
    for card_x, card_y  in sizes:
        x1, y1 = max([wallet_x, card_x]), max([wallet_y, card_y])
        x2, y2 = max([wallet_x, card_y]), max([wallet_y, card_x])
        
        if x1 * y1 <= x2 * y2:
            wallet_x, wallet_y = x1, y1
        else:
            wallet_x, wallet_y = x2, y2
    return wallet_x * wallet_y