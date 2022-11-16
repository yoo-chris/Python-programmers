def solution(order):
    answer = 0
    for i in str(order):
        if i in ["3","6","9"]:
            answer += 1
    return answer

#포문으로 한자리씩 뺴가면서 하는건 왜 안되는거지