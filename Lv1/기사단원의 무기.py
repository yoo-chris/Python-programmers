def solution(number, limit, power):
    #제곱근 생각 -> 다시 풀어보기
    answer = 0
    atk = []
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 1
                if j ** 2 != i:
                    count += 1
            if count > limit:
                count = power
                break
        answer += count
        
    return answer