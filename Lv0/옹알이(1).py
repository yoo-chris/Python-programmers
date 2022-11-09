def solution(babbling):
    answer = 0
    for i in range(0,len(babbling)):
        del_aya=babbling[i].replace("aya","!!!")
        del_ye=del_aya.replace("ye","!!")
        del_woo=del_ye.replace("woo","!!!")
        del_ma=del_woo.replace("ma","!!")
        if len(del_ma) == del_ma.count('!'):
            answer += 1
    return answer