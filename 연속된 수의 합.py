def solution(num, total):
    answer = []
    n = total // num
    answer.append(n)
    sum = n
    i = 1
    while (sum != total) or (len(answer) != num):
        sum += (n+i)
        answer.append(n+i)
        if len(answer) == num:
            break
        sum += (n-i)
        answer.append(n-i)
        i += 1
    answer.sort()
    return answer