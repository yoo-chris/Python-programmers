def solution(board, moves):
    answer = 0
    toy = []
    n = len(board)      #길이 n짜리 정사각
    t = 0
    #moves인덱스 변경
    for i in range(0,len(moves)):
        moves[i] -= 1
        
    for i in range(0,len(moves)):
        for j in range(0,n):
            if board[j][moves[i]] != 0:
                toy.append(board[j][moves[i]])
                board[j][moves[i]] = 0
                break
    while True:
        if t == len(toy)-1 or len(toy) == 0:
            break
        if toy[t] == toy[t+1]:
            answer += 2
            toy.pop(t)
            toy.pop(t)
            t = -1
        t += 1
    return answer