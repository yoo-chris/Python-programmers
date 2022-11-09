def solution(num_list):
    #num_list.reverse()
    answer = []
    for i in range(len(num_list)-1, -1, -1):
        answer.append(num_list[i])
    return answer