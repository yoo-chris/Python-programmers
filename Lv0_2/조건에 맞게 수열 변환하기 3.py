def solution(arr, k):
    answer = []
    if k % 2 == 1:
        for i in range(0,len(arr)):
            arr[i] *= k
    else:
        for i in range(0,len(arr)):
            arr[i] += k
            
    return arr