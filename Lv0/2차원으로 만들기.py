def solution(num_list, n):
    answer = []
    num_list.reverse()
    for i in range(0,len(num_list)//n):
        test = []
        for j in range(0,n):
            test.append(num_list.pop())
        answer.append(test)
    
    return answer