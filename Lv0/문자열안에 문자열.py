def solution(str1, str2):
    answer = 2
    t = str1.find(str2)
    if t >= 0:
        answer = 1
    return answer