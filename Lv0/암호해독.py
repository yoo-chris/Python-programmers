def solution(cipher, code):
    answer = ''
    t = len(cipher) // code
    for i in range(1,t+1):
        answer += cipher[i*code - 1]
    return answer