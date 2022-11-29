def solution(s):
    answer = False
    s = list(s)
    count_num = 0
    
    for i in s:
        if '0' <= i <= '9':
            count_num += 1
    
    if (len(s) == 4 or len(s) == 6) and (count_num == len(s)):
        answer = True
    
    return answer