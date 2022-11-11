
def solution(my_string):
    answer = 0
    for i in range(0,len(my_string)):
        if '1' <= my_string[i] <= '9':
            t = int(my_string[i])
            answer += t
    return answer