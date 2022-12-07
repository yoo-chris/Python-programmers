def solution(k, score):
    answer = []
    n = []
    for i in range(0,len(score)):
        n.append(score[i])
        n.sort()
        if len(n) > k:
            n = n[len(n)-k:len(n)]
        answer.append(n[0])
    return answer