import sys

def insert_sort(nums):
    for i in range(1,len(nums)):
        save = nums[i]
        j = i
        while j > 0 and nums[j - 1] > save:#找到新插入数据应处的位置
            nums[j] = nums[j - 1]
            j -= 1
        nums[j] = save
    

if __name__ == '__main__':
    nums = [10,8,4,-1,2,6,7,3]
    print 'nums is',nums
    insert_sort(nums)
    print 'nums is',nums