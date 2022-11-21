def solution(s):
    answer = ''
    t = len(s) // 2
    if len(s) % 2 == 0:
        answer += s[t-1]
        answer += s[t]
    else:
        answer += s[t]
    return answer