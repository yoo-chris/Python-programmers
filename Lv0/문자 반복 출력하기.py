def solution(my_string, n):
    answer = ''
    for i in range(0,len(my_string)):
        answer += n * my_string[i]
    return answer