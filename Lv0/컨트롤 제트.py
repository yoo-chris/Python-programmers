def solution(s):
    answer = 0
    n = []
    s2 = s.split()
    if s2[0] == 'Z':
        s2[0] = '0'
        
    for i in range(0,len(s2)):
        if s2[i] == 'Z':
            answer -= n.pop()
        else:
            n.append(int(s2[i]))
            answer += int(s2[i])
    return answer