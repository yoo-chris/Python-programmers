def solution(my_string):
    answer = []
    for i in range(0,len(my_string)):
        if '0' <= my_string[i] <= '9':
            answer.append(int(my_string[i]))
    answer.sort()
    return answer