def solution(s):
    answer = True
    for i in range(0,len(s)):
        if (s.count('p') + s.count('P')) != (s.count('y') + s.count('Y')):
            answer = False
            
    return answer