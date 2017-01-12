import math
import sys

def count_sort(nums):
    min = sys.maxint
    max = 0
    # 取得最大值和最小值
    for x in nums:
        if x > max:
            max = x
        if x < min:
            min = x
    # 创建数组C
    count = [0] * (max - min +1)
    for index in nums:
        count[index - min] += 1
    index = 0
    # 填值
    for a in range(max - min+1):
        for c in range(count[a]):
            nums[index] = a + min
            index += 1


if __name__ == '__main__':
    nums = [10,8,4,1,2,6,7,3]
    print 'nums is',nums
    count_sort(nums)
    print 'nums is',nums