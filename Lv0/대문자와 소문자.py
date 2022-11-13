def solution(my_string):
    answer = ''
    for i in my_string:
        if 'a' <= i <= 'z':
            answer += i.upper()
        else:
            answer += i.lower()
    return answer