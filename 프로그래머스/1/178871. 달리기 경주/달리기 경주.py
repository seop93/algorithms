def solution(players, callings):
    dict_sol = {key: i for i, key in enumerate(players)}

    for player in callings:
        c = dict_sol[player]
        dict_sol[player] -= 1
        dict_sol[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]
    return players
