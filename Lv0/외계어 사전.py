def solution(spell, dic):
    answer = 0
    count = 0
    for i in range(0,len(dic)):
        for j in range(0,len(spell)):
            dic[i] = dic[i].replace(spell[j],'!',1)
            
    for i in range(0,len(dic)):
        if dic[i].count('!') == len(spell):
            count += 1
    if count > 0:
        answer = 1
    else:
        answer = 2
    return answer