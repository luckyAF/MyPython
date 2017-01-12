def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    temp = {}
    i = 0
    for num in nums:
        if num in temp:
            return [temp[num],i]
        else:
            temp[target-num] = i
        
        i = i + 1
    