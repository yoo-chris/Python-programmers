def solution(numbers, hand):
    answer = ''
    #   1 2 3
    #   4 5 6
    #   7 8 9
    #   * 0 #
    
    l_a = 3
    l_b = 0
    r_a = 3
    r_b = 2
    
    for i in range(0,len(numbers)):
        if numbers[i] == 1:
            answer += 'L'
            l_a = 0
            l_b = 0
        elif numbers[i] == 2:   #0 1
            if (abs(l_a - 0) + abs(l_b - 1)) < (abs(r_a - 0) + abs(r_b - 1)):
                answer += 'L'
                l_a = 0
                l_b = 1
            elif (abs(l_a - 0) + abs(l_b - 1)) > (abs(r_a - 0) + abs(r_b - 1)):
                answer += 'R'
                r_a = 0
                r_b = 1
            else:
                if hand == 'left':
                    answer += 'L'
                    l_a = 0
                    l_b = 1
                else:
                    answer += 'R'
                    r_a = 0
                    r_b = 1
        elif numbers[i] == 3:
            answer += 'R'
            r_a = 0
            r_b = 2
            
        elif numbers[i] == 4:
            answer += 'L'
            l_a = 1
            l_b = 0
            
        elif numbers[i] == 5:   #1 1
            if (abs(l_a - 1) + abs(l_b - 1)) < (abs(r_a - 1) + abs(r_b - 1)):
                answer += 'L'
                l_a = 1
                l_b = 1
            elif (abs(l_a - 1) + abs(l_b - 1)) > (abs(r_a - 1) + abs(r_b - 1)):
                answer += 'R'
                r_a = 1
                r_b = 1
            else:
                if hand == 'left':
                    answer += 'L'
                    l_a = 1
                    l_b = 1
                else:
                    answer += 'R'
                    r_a = 1
                    r_b = 1
                
        elif numbers[i] == 6:
            answer += 'R'
            r_a = 1
            r_b = 2
            
        elif numbers[i] == 7:
            answer += 'L'
            l_a = 2
            l_b = 0
            
        elif numbers[i] == 8:   #2 1
            if (abs(l_a - 2) + abs(l_b - 1)) < (abs(r_a - 2) + abs(r_b - 1)):
                answer += 'L'
                l_a = 2
                l_b = 1
            elif (abs(l_a - 2) + abs(l_b - 1)) > (abs(r_a - 2) + abs(r_b - 1)):
                answer += 'R'
                r_a = 2
                r_b = 1
            else:
                if hand == 'left':
                    answer += 'L'
                    l_a = 2
                    l_b = 1
                else:
                    answer += 'R'
                    r_a = 2
                    r_b = 1
            
        elif numbers[i] == 9:
            answer += 'R'
            r_a = 2
            r_b = 2
            
        elif numbers[i] == 0:   #3 1
            if (abs(l_a - 3) + abs(l_b - 1)) < (abs(r_a - 3) + abs(r_b - 1)):
                answer += 'L'
                l_a = 3
                l_b = 1
            elif (abs(l_a - 3) + abs(l_b - 1)) > (abs(r_a - 3) + abs(r_b - 1)):
                answer += 'R'
                r_a = 3
                r_b = 1
            else:
                if hand == 'left':
                    answer += 'L'
                    l_a = 3
                    l_b = 1
                else:
                    answer += 'R'
                    r_a = 3
                    r_b = 1
            
    return answer