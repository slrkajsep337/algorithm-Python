

#달리기 경주
def solution(players, callings):
    idx = {}
    for i in range(len(players)):
        p = players[i]
        idx[p] = i

    for c in callings:
        i = idx[c]
        players[i-1], players[i] = players[i], players[i-1]
        idx[players[i-1]], idx[players[i]] = idx[players[i]], idx[players[i-1]]


    return players