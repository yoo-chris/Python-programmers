def solution(numbers):
    answer = ''
    a = numbers.replace('one','1')
    b = a.replace('two','2')
    c = b.replace('three','3')
    d = c.replace('four','4')
    e = d.replace('five','5')
    f = e.replace('six','6')
    g = f.replace('seven','7')
    h = g.replace('eight','8')
    i = h.replace('nine','9')
    j = i.replace('zero','0')
    return int(j)