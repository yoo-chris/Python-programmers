def solution(age):
    list = ['a','b','c','d','e','f','g','h','i','j']
    answer = ''
    
    while age > 0:
        answer += list[age%10]
        age = age // 10
    result = "".join(reversed(answer))
    return result