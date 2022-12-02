def solution(s):
    answer = ''
    s = s.split(" ")
    
    for i in range(0,len(s)):
        s[i] = s[i].capitalize()
        answer += s[i]
        if i == len(s)-1:
            break
        answer += ' '
    
    return answer