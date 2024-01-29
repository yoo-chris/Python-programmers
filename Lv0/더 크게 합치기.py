def solution(a, b):
    answer_str1 = ''
    answer_str2 = ''
    
    answer_str1 = str(a) + str(b)
    answer_str2 = str(b) + str(a)
    if int(answer_str1) > int(answer_str2):
        return int(answer_str1)
    else:
        return int(answer_str2)