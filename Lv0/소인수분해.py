def solution(n):
    answer = []
    for i in range(2,10000):
        count = 0
        while n % i == 0:
            n = n // i
            count += 1
        if count >= 1:
            answer.append(i)
        if n == 1:
            break
    return answer