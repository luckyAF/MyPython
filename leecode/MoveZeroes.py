def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    length = len(nums);
   
    for i in range(length-1):
        j = i
        if nums[i] == 0:
            while j < length -1 and nums[j] == 0:
                j = j +1
            nums[i],nums[j] = nums[j],nums[i]
        
    print(nums)


array = [0,0,0,1,0,0,2,3,0,4,5,0]
array2 = [1,0,2,0]
moveZeroes(array2)