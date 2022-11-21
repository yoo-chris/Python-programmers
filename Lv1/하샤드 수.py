def solution(x):
    answer = True
    x1 = x
    t = 0
    while x > 0:
        t += x % 10
        x = x // 10
    if x1 % t != 0:
        answer = False
    return answer