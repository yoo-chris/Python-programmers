def solution(n):
    answer = 1
    result = 0
    for i in range(1,11):
        answer *= i
        if answer <= n:
            result = i
    return result