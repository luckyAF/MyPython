import sys
def getMax(nums):
    max = nums[0]
    sum = 0
    for value in nums:
        sum = sum + value
        if sum > max :
            max = sum
        if sum < 0:
            sum = 0
    return max

numbers = [-4,-1,-1,-1,-1,-2,-1,-5]
print(getMax(numbers))