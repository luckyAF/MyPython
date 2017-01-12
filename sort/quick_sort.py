import sys

def quick_sort(nums,left,right):
    if left >= right:
        return
    key = nums[left]
    low = left
    high = right
    while left < right:
        while left < right and nums[right] >= key:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= key:
            left += 1
        nums[right] = nums[left]
    nums[right] = key
    quick_sort(nums,low,left - 1)
    quick_sort(nums,left + 1, high)


if __name__ == '__main__':
    nums = [10,8,4,-1,2,6,7,3]
    print 'nums is',nums
    quick_sort(nums,0,len(nums)-1)
    print 'nums is',nums