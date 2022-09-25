nums = list(range(5))
print(sum(nums))



def sum(nums):
    if(len(nums) == 1):
        return nums[0]
    else: 
        return nums[0] + sum(nums[1:])
