def solution(babbling):
    answer = 0
    # 1 - aya , 2 - ye , 3 - woo , 4 - ma
    for i in range(0,len(babbling)):
        babbling[i] = babbling[i].replace('aya', '1')
        babbling[i] = babbling[i].replace('ye', '2')
        babbling[i] = babbling[i].replace('woo', '3')
        babbling[i] = babbling[i].replace('ma', '4')
    
    for i in range(0,len(babbling)):
        count = 0
        if len(babbling[i]) == 1 and '1' <= babbling[i][0] <= '4':
            answer += 1
        elif len(babbling[i]) > 1:
            #숫자로만 이루어져 있는지 물어보는 if문
            if  len(babbling[i]) == babbling[i].count('1') + babbling[i].count('2') + babbling[i].count('3') + babbling[i].count('4'):
                for j in range(0,len(babbling[i])-1):
                    #숫자가 중복되는지 -> 중복되면 무효
                    if babbling[i][j] == babbling[i][j+1]:
                        count += 1
                if count == 0:
                    answer += 1
            
    return answer