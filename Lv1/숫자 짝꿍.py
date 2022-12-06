def solution(X, Y):
    #진짜 골치 아픈 문제였다..
    answer = ''
    Z = ['9','8','7','6','5','4','3','2','1','0']
    i = 0
    a = 0
    b = 0
    while i != len(Z):
        a = X.count(Z[i])
        b = Y.count(Z[i])
        t = min(a,b)
        answer += Z[i] * t
        i += 1
    
    if len(answer) == 0:
        return "-1"
    if len(answer) == answer.count('0'):
        return "0"
    return answer