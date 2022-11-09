def solution(quiz):
    answer = []
    result = []
    t=0
    for i in range(0,len(quiz)):
        answer.append(quiz[i].split(" "))
        for j in range(0,len(answer[i])):
            if answer[i][1] == '+':
                t = int(answer[i][0]) + int(answer[i][2])
            else:
                t = int(answer[i][0]) - int(answer[i][2])
        if t == int(answer[i][4]):
            result.append('O')
        else:
            result.append('X')
    return result