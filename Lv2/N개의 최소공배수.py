def solution(arr):
    answer = 0
    arr.sort()
    mul = arr[0]
    for i in range(1,len(arr)):
        a = arr[i]
        if mul > a:
            tmp = a
            a = mul
            mul = tmp
        for j in range(a, mul*a + 1):
            if j % a == 0 and j % mul == 0:
                mul = j
                break
    return mul
        