def solution(survey, choices):
    answer = ''
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(0,len(survey)):
        #AN
        if survey[i][0] == 'A':
            if choices[i] == 1:
                dic['A'] += 3
            elif choices[i] == 2:
                dic['A'] += 2
            elif choices[i] == 3:
                dic['A'] += 1
            elif choices[i] == 4:
                dic['N'] += 0
            elif choices[i] == 5:
                dic['N'] += 1
            elif choices[i] == 6:
                dic['N'] += 2
            elif choices[i] == 7:
                dic['N'] += 3
        #NA
        if survey[i][0] == 'N':
            if choices[i] == 1:
                dic['N'] += 3
            elif choices[i] == 2:
                dic['N'] += 2
            elif choices[i] == 3:
                dic['N'] += 1
            elif choices[i] == 4:
                dic['N'] += 0
            elif choices[i] == 5:
                dic['A'] += 1
            elif choices[i] == 6:
                dic['A'] += 2
            elif choices[i] == 7:
                dic['A'] += 3
        #CF
        if survey[i][0] == 'C':
            if choices[i] == 1:
                dic['C'] += 3
            elif choices[i] == 2:
                dic['C'] += 2
            elif choices[i] == 3:
                dic['C'] += 1
            elif choices[i] == 4:
                dic['C'] += 0
            elif choices[i] == 5:
                dic['F'] += 1
            elif choices[i] == 6:
                dic['F'] += 2
            elif choices[i] == 7:
                dic['F'] += 3
        #FC
        if survey[i][0] == 'F':
            if choices[i] == 1:
                dic['F'] += 3
            elif choices[i] == 2:
                dic['F'] += 2
            elif choices[i] == 3:
                dic['F'] += 1
            elif choices[i] == 4:
                dic['F'] += 0
            elif choices[i] == 5:
                dic['C'] += 1
            elif choices[i] == 6:
                dic['C'] += 2
            elif choices[i] == 7:
                dic['C'] += 3
        #JM
        if survey[i][0] == 'J':
            if choices[i] == 1:
                dic['J'] += 3
            elif choices[i] == 2:
                dic['J'] += 2
            elif choices[i] == 3:
                dic['J'] += 1
            elif choices[i] == 4:
                dic['J'] += 0
            elif choices[i] == 5:
                dic['M'] += 1
            elif choices[i] == 6:
                dic['M'] += 2
            elif choices[i] == 7:
                dic['M'] += 3
        #MJ
        if survey[i][0] == 'M':
            if choices[i] == 1:
                dic['M'] += 3
            elif choices[i] == 2:
                dic['M'] += 2
            elif choices[i] == 3:
                dic['M'] += 1
            elif choices[i] == 4:
                dic['M'] += 0
            elif choices[i] == 5:
                dic['J'] += 1
            elif choices[i] == 6:
                dic['J'] += 2
            elif choices[i] == 7:
                dic['J'] += 3
        #RT
        if survey[i][0] == 'R':
            if choices[i] == 1:
                dic['R'] += 3
            elif choices[i] == 2:
                dic['R'] += 2
            elif choices[i] == 3:
                dic['R'] += 1
            elif choices[i] == 4:
                dic['R'] += 0
            elif choices[i] == 5:
                dic['T'] += 1
            elif choices[i] == 6:
                dic['T'] += 2
            elif choices[i] == 7:
                dic['T'] += 3
        #TR
        if survey[i][0] == 'T':
            if choices[i] == 1:
                dic['T'] += 3
            elif choices[i] == 2:
                dic['T'] += 2
            elif choices[i] == 3:
                dic['T'] += 1
            elif choices[i] == 4:
                dic['T'] += 0
            elif choices[i] == 5:
                dic['R'] += 1
            elif choices[i] == 6:
                dic['R'] += 2
            elif choices[i] == 7:
                dic['R'] += 3
    #RT
    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    #CF
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    #JM
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    #AN
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'
                
                
            
    return answer