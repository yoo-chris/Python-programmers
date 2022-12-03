def solution(s):
    answer = ''
    s = list(s)
    s.sort(reverse = True)
    for i in range(0,len(s)):
        answer += s[i]
    return answer