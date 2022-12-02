def solution(s):
    answer = []
    change = 0
    del_zero = 0
    t = bin(6)
    while len(s) != 1:
        del_zero += s.count('0')
        s = s.replace('0', '')
        t = bin(len(s))
        s = ''
        for i in range(2,len(t)):
            s += t[i]
        change += 1
    answer.append(change)
    answer.append(del_zero)
    return answer