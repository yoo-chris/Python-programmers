def solution(num_list):
    answer = []
    num_list.sort()
    for i in range(5, len(num_list)):
        answer.append(num_list[i])
    return answer