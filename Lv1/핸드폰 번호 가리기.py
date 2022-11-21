def solution(phone_number):
    answer = ''
    num = ''
    for i in range(len(phone_number)-4, len(phone_number)):
        num += phone_number[i]
    
    for i in range(0,len(phone_number)-4):
        answer += '*'
        
    answer += num
    
    return answer