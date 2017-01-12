import sys

def bubble_sort(nums):
    count = len(nums)
    for i in range(0, count):
        for j in range(i + 1, count):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    
if __name__ == '__main__':
    nums = [10,8,4,-1,2,6,7,3]
    print 'nums is',nums
    bubble_sort(nums)
    print 'nums is',nums