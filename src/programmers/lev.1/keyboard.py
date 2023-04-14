

#대충 만든 자판

#내풀이 3중포문 ..
def solution(keymap, targets):
    answer = []

    for target in targets:
        result = 0
        for t in target:
            cnt = 101
            for key in keymap:
                if t in key and key.index(t ) + 1 <cnt:
                    cnt = key.index(t ) +1
            if cnt == 101:
                result = -1
                break
            result += cnt
        answer.append(result)

    return answer


#다른 풀이 - 속도 더 빠름
def solution2(keymap, targets):
    kdist = dict()
    #키보드의 알파벳들에 값을(몇번 눌러야하는지) 미리 매칭해둠
    for s in keymap :
        for i in range(len(s)) :
            kdist.setdefault(s[i],100)
            kdist[s[i]] = min(kdist[s[i]],i+1)
    ans = []
    for s in targets :
        cnt = 0
        flag=0
        for i in range(len(s)) :
            if s[i] not in kdist :
                flag=1
                break
            cnt += kdist[s[i]]
        if flag==1 : ans.append(-1)
        else : ans.append(cnt)
    return ans