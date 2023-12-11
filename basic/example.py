def solution(players, callings):
    dict_sol = {key: i for i, key in enumerate(players)}

    for p in callings:
        c = dict_sol[p]
        dict_sol[p] -= 1
        dict_sol[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]
    return dict_sol.keys()
