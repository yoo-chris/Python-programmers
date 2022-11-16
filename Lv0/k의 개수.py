def solution(i, j, k):
    answer = 0
    for a in range(i, j+1):
        while a > 0:
            t = a % 10
            a = a // 10
            if t == k:
                answer += 1
    return answer