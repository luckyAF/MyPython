import sys

    ''''' 选择排序
    '''
def select_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    

if __name__ == '__main__':
    nums = [10,8,4,-1,2,6,7,3]
    print 'nums is',nums
    select_sort(nums)
    print 'nums is',nums