def solution(board):
    answer = 0
    count = 0
    bomb = []
    a=0
    b=0
    
    #지뢰의 인덱스를 저장할 배열 만들기
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if (board[i][j] == 1):
                t = []
                t.append(i)
                t.append(j)
                bomb.append(t)
    
    for a in range(0,len(bomb)):
        if len(board) == 1:
            break
                
        i = bomb[a][0]
        j = bomb[a][1]
        if i == 0:
            if j == 0:              #1 맨 왼쪽위
                board[i][j+1] = 1   #오른쪽
                board[i+1][j+1] = 1 #오른쪽 아래
                board[i+1][j] = 1   #아래
                        
            elif j == len(board)-1:   #2 맨 오른쪽위
                board[i][j-1] = 1   #왼쪽
                board[i+1][j-1] = 1 #왼쪽 아래
                board[i+1][j] = 1   #아래
                        
            else:                   #3 맨 윗줄
                board[i][j+1] = 1   #오른쪽
                board[i+1][j] = 1   #아래
                board[i][j-1] = 1   #왼쪽
                board[i+1][j-1] = 1 #왼쪽 아래
                board[i+1][j+1] = 1 #오른쪽 아래
                        
        elif i == len(board)-1:
            if j == 0:              #4 맨 왼쪽아래
                board[i-1][j] = 1   #위
                board[i][j+1] = 1   #오른쪽
                board[i-1][j+1] = 1 #오른쪽 위
                        
            elif j == len(board)-1:   #5 맨 오른쪽아래
                board[i-1][j] = 1   #위
                board[i][j-1] = 1   #왼쪽
                board[i-1][j-1] = 1 #왼쪽 위
                        
            else:                   #6 맨아랫줄
                board[i-1][j] = 1   #위
                board[i][j+1] = 1   #오른쪽
                board[i][j-1] = 1   #왼쪽
                board[i-1][j+1] = 1 #오른쪽 위
                board[i-1][j-1] = 1 #왼쪽 위
                        
        else:
            if j == 0:              #7 왼쪽중앙
                board[i-1][j] = 1   #위
                board[i+1][j] = 1   #아래
                board[i][j+1] = 1   #오른쪽
                board[i-1][j+1] = 1 #오른쪽 위
                board[i+1][j+1] = 1 #오른쪽 아래
                        
            elif j == len(board)-1:   #8 오른쪽중앙
                board[i-1][j] = 1   #위
                board[i+1][j] = 1   #아래
                board[i][j-1] = 1   #왼쪽
                board[i-1][j-1] = 1 #왼쪽 위
                board[i+1][j-1] = 1 #왼쪽 아래
                        
            else:                   #9 나머지
                board[i-1][j] = 1   #위
                board[i][j+1] = 1   #오른쪽
                board[i+1][j] = 1   #아래
                board[i][j-1] = 1   #왼쪽
                board[i+1][j+1] = 1 #오른쪽 아래
                board[i-1][j+1] = 1 #오른쪽 위
                board[i-1][j-1] = 1 #왼쪽 위
                board[i+1][j-1] = 1 #왼쪽 아래
                
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j] == 0:
                answer += 1
    
    return answer