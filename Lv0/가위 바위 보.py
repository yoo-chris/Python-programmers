def solution(rsp):
    answer = ''
    for i in range(0,len(rsp)):
        if rsp[i] == '0':
            answer += '5'
        elif rsp[i] == '2':
            answer += '0'
        else:
            answer += '2'
    return answer