def solution(s):
    answer = ''
    a = []
    c = ''
    test = 'one'
    for i in range(0,len(s)):
        if '0' <= s[i] <= '9':
            answer += s[i] 
        else:
            c += s[i]
        
        if c == 'zero':
            answer += '0'
            c = ''
        if c == 'one':
            answer += '1'
            c = ''
        if c == 'two':
            answer += '2'
            c = ''
        if c == 'three':
            answer += '3'
            c = ''
        if c == 'four':
            answer += '4'
            c = ''
        if c == 'five':
            answer += '5'
            c = ''
        if c == 'six':
            answer += '6'
            c = ''
        if c == 'seven':
            answer += '7'
            c = ''
        if c == 'eight':
            answer += '8'
            c = ''
        if c == 'nine':
            answer += '9'
            c = ''
    
    return int(answer)