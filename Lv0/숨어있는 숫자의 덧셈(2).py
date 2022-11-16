def solution(my_string):
    answer = 0
    result = []
    for i in range(0,len(my_string)):
        t=''
        if i > 0 and '0' <= my_string[i-1] <= '9':
            continue
        if '0' <= my_string[i] <= '9':
            for j in range(i, len(my_string)):
                if '0' <= my_string[j] <= '9':
                    t += my_string[j]
                else:
                    break
            result.append(t)
    for i in range(0,len(result)):
        answer += int(result[i])
    return answer