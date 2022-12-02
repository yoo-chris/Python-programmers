def solution(s):
    answer = ''
    num = []
    s = s.split(" ")
    for i in range(0,len(s)):
        num.append(int(s[i]))
    num.sort()
    
    answer += str(num[0])
    answer += " "
    answer += str(num[len(num)-1])
    return answer