def solution(nums):
    answer = 0
    total = []
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                total.append(nums[i]+nums[j]+nums[k])
    total.sort()
    
    for i in range(0,len(total)):
        count = 0
        for j in range(1,total[i]+1):
            if total[i] % j == 0:
                count += 1
        if count == 2:
            answer += 1
            
    return answer