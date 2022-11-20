def solution(array):
    dic = {}
    for n in array:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    
    if len(dic) == 1:
        return dic[0][0]
    
    if dic[0][1] != dic[1][1]:
        return dic[0][0]
    else:
        return -1
    return dic