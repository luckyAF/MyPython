import sys
import math
 
def radix_sort(a, radix=10):
    """a为整数列表， radix为基数"""
    K = int(math.ceil(math.log(max(a), radix))) # 用K位数可表示任意整数
    bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
    for i in range(1, K+1): # K次循环
        for val in a:
            bucket[val%(radix**i)/(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
        del a[:]
        for each in bucket:
            a.extend(each) # 桶合并
        bucket = [[] for i in range(radix)]

if __name__ == '__main__':
    nums = [130,228,433,11,342,56,27,33]
    print 'nums is',nums
    radix_sort(nums,10)
    print 'nums is',nums