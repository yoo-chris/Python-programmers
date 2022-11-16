def solution(keyinput, board):
    answer = [0,0]
    for i in range(0,len(keyinput)):
        if keyinput[i] == 'up':
            answer[1] += 1
            if abs(answer[1]) > board[1] // 2:
                answer[1] -= 1
        elif keyinput[i] == 'down':
            answer[1] -= 1
            if abs(answer[1]) > board[1] // 2:
                answer[1] += 1
        elif keyinput[i] == 'right':
            answer[0] += 1
            if abs(answer[0]) > board[0] // 2:
                answer[0] -= 1
        else:
            answer[0] -= 1
            if abs(answer[0]) > board[0] // 2:
                answer[0] += 1
    return answer