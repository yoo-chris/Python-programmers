def solution(n):
    answer = 0
    cnt_1 = bin(n).count('1')
    n += 1
    while bin(n).count('1') != cnt_1:
        n += 1
        
    return n