#Done on LeetCode

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        #found = False
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        else:
            while lower < upper:
                mid = (lower + upper) // 2
                if nums[upper] == target:
                    return upper
                if nums[lower] == target:
                    return lower
                
                if nums[mid] == target:
                    #found = True
                    return mid
                elif target < nums[mid]:
                    upper = mid - 1
                else:
                    lower = mid + 1

        return -1

# ALl 47 test cases passed