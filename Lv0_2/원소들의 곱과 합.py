def solution(num_list):
    answer = 0
    num1 = 1
    for i in range(0,len(num_list)):
        num1 *= num_list[i]
    num2 = sum(num_list) * sum(num_list)
    if num1 < num2:
        return 1
    else:
        return 0