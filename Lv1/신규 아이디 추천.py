def solution(new_id):
    #1단계 대문자 -> 소문자
    new_id = new_id.lower()
    
    #2단계 알파벳소문자, - _ .빼고 다 지우기
    i = 0
    while i != len(new_id):
        if new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.' or 97 <= ord(new_id[i]) <= 122 or '0'<= new_id[i] <= '9':
            i += 0
        else:
            new_id = new_id.replace(new_id[i], '', 1)
            i -= 1
        i += 1
    
    
    #3단계 ..을 .로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    #4단계 처음이나 끝의 .제거 + 둘 다 제거해야함
    #startswith랑 endswith는 왜 쓰지 못할까?
    if new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id[1:]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
        
    #5단계 빈문자열이면 a추가
    if len(new_id) == 0:
        new_id += 'a'
    
    #6단계 15개이상이면 15개까지 끊기 + 마지막이 . 이면 제거
    if len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
        
    #7단계 2자 이하면 마지막 문자를 길이가 3될때까지 반복
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]
    
    return new_id