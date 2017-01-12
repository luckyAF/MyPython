import sys

'''''
希尔排序
'''
def shell_sort(nums):
    nums_len = len(nums)
    gap = nums_len / 2 # 增量
    while gap > 0:
        for i in range(nums_len):
            m = i
            j = i + 1
            while j < nums_len:
                if nums[j] < nums[m]:
                    m = j
                j += gap
            if m != i:
                nums[m],nums[i] =nums[i],nums[m]
        gap /= 2


if __name__ == '__main__':
    nums = [12,8,4,-1,2,6,7,3]
    print 'nums is',nums
    shell_sort(nums)
    print 'nums is',nums