def solution(s):
    answer = True
    count = 0
    
    for i in range(0,len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            answer = False
    
    if count != 0:
        answer = False
    return answer