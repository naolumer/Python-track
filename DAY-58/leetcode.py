
def JumpGame( nums:list):
    
    n= len(nums)
    goal=n-1

    for i in range(n-1,-1,-1):
        if i+ nums[i] >= goal:
            goal=i
    return goal==0
