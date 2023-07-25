def solution(players, callings):
    ranking_dict = {players[i] : i for i in range(len(players))}
    for calling in callings:
        idx = ranking_dict[calling]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        ranking_dict[players[idx - 1]] -= 1
        ranking_dict[players[idx]] += 1
    return players