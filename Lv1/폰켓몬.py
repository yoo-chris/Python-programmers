def solution(nums):
    answer = 0
    n = []
    nums.sort()
    n.append(nums[0])
    
    for i in range(1,len(nums)):
        if nums[i] in nums[0:i]:
            continue
        else:
            n.append(nums[i])
    
    if len(n) >= len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(n)
    return answer