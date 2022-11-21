def solution(x, n):
    answer = []
    t=0
    for i in range(0,n):
        t += x
        answer.append(t)
    return answer