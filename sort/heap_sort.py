#数组编号 从0开始
def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

#保持最大堆性质 是以i为根的子树成为最大堆
def max_heapify(nums, i ,heap_size):
    if heap_size <= 0:
        return
    l = left(i)
    r = right(i);
    largest = i #选出子节点中较大的节点 
    if  l < len(nums) and nums[l] > nums[largest]:
        largest = l;
    if  r < len(nums) and nums[r] > nums[largest]:
        largest = r
    if i != largest: #说明当前节点不是最大的，下移
        nums[i],nums[largest] = nums[largest],nums[i]
        max_heapify(nums,largest,heap_size) 

#  建堆
def build_max_heap(nums):
    heap_size = len(nums)
    if heap_size > 1 :
        node = heap_size / 2 - 1
        while node >= 0 :
            max_heapify(nums, node, heap_size)
            node -= 1

# 堆排序 下标从0开始
def heap_sort(nums):
    build_max_heap(nums)
    heap_size = len(nums)
    i = heap_size - 1
    while i > 0:
        nums[0],nums[i] = nums[i],nums[0] # 对中的最大值存入数组适当的位置，并且进行交换
        heap_size -= 1    # heap 大小 递减1
        i -= 1  # 存放堆中最大值的下标递减 1
        max_heapify(nums,0,heap_size)


if __name__ == '__main__':
    nums = [12,8,4,-1,2,6,7,3]
    print 'nums is',nums
    heap_sort(nums)
    print 'nums is',nums