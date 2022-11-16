def solution(s):
    answer = ''
    s = "".join(sorted(s))
    for i in range(0,len(s)):
        if len(s) == 1:
            answer += s[0]
            break
        if i == 0:
            if s[i] != s[i+1]:
                answer += s[i]
        elif i == len(s)-1:
            if s[i] != s[i-1]:
                answer += s[i]
        else:
            if s[i] != s[i-1] and s[i] != s[i+1]:
                answer += s[i]
    return answer