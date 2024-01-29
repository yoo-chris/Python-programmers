def solution(keymap, targets):
    answer = []
    
    for a in range(0,len(targets)):
        sum = 0
        for b in range(0,len(targets[a])):
            YN = False
            f = 100
            for c in range(0,len(keymap)):
                if targets[a][b] in keymap[c]:
                    f=min(keymap[c].index(targets[a][b])+1, f)
                    YN = True
                    
            if YN == False:
                sum = -1
                break
            else:
                sum += f
        answer.append(sum)
    return answer