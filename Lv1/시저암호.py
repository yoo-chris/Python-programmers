def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(0,len(s)):
        if s[i] == ' ':
            answer += ' '
            continue
        a = ord(s[i])
        if 65 <= a <= 90:
            a = 65 + (a - 65 + n) % 26
        else:
            a = 97 + (a - 97 + n) % 26
        b = chr(a)
        answer += b
    return answer