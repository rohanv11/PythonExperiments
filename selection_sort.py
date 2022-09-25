nums = [45, 238, 15, 27, 89, 45, 100, 54, -1, 90, -155]



def selection_sort(nums):

    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    print(nums)

selection_sort(nums)