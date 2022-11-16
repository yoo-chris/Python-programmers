def solution(bin1, bin2):
    answer = ''
    answer1 = 0
    
    bin_1 = int(bin1)
    bin_2 = int(bin2)
    
    #변환결과 -> result_?
    result_1 = 0    
    result_2 = 0
    result = 0      #r1+r2
    i=1
    j=1
    
    while bin_1 > 0:
        t = bin_1 % 10
        result_1 += t * i
        bin_1 = bin_1 // 10
        i = i * 2
        
    while bin_2 > 0:
        t = bin_2 % 10
        result_2 += t * j
        bin_2 = bin_2 // 10
        j = j * 2
    
    result = result_1 + result_2
    
    answer1 = bin(result)
    for i in range(2,len(answer1)):
        answer += str(answer1[i])
    return answer