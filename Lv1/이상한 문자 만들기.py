def solution(s):
    answer = ''
    s = list(s)
    n = 1
    
    for i in range(0,len(s)):
        if s[i] == ' ':
            n = 0
        if n % 2 != 0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
        n += 1
    
    for i in range(0,len(s)):
        answer += s[i]
    return answer